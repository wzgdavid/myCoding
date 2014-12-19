#!/usr/bin/python
#coding=utf8
# https://github.com/unbit/uwsgi/blob/master/tests/wss_chat.py
#
# uwsgi --socket 127.0.0.1:3031 --wsgi-file foobar.py --master --processes 4 
#       --threads 2 --stats 127.0.0.1:9191
#
# uwsgi --http-socket :9090 --gevent 100 --module w --gevent-monkey-patch
#uwsgi --http-socket 0.0.0.0:8081 --gevent 100 --module w --gevent-monkey-patch
# version 1.0, working now. Apr/14/2014
#
# ToDo:
#   ws://#.#.#.#/ws?api=new&uid=##&sig=##&arg=##&timestamp=##
#       to start new connection
#
#   ws://#.#.#.#/ws?api=sub&channels=##,##&uid=##&sig=##&arg=##&timestamp=##
#       to subscribe
#
#   ws://#.#.#.#/ws?api=msg&&uid=##&msg=...&sig=##&arg=##&timestamp=##
#       to send message
#
#   #old one:
#   ws://#.#.#.#/ws?api=pub&&uid=##&content=...&sig=##&arg=##&timestamp=##
#       to send message

import uwsgi
import time
import gevent.select
import redis
import urlparse
import json
#from ws_sig_auth import ws_sig_auth
r = redis.Redis(host='172.31.5.116', port=6379, db=14)

active_users = {}   #uid:active_time

def application(env, start_response):
    global active_users
    print '\nPATH_INFO=', env['PATH_INFO']

    if env['PATH_INFO'] == '/':
        start_response('200 OK', [('Content-Type','text/html')])
        return "Websocket serve is running, visit at: ws://.../ws/"

    elif env['PATH_INFO'] == '/favicon.ico':
        return ""


    elif env['PATH_INFO'] == '/ws':    
        #subscribe to foobar? Only allow user's friend to subscribe ?
        #websocket request need auth:
        
        for s in env:
            print 'Environ:', s, ':', env[s]

        qs = env.get('QUERY_STRING')
        query_dict = dict(urlparse.parse_qsl(qs))
        
#       if not ws_sig_auth(query_dict=query_dict):
#           return 'Unauthorized.'

        uwsgi.websocket_handshake(env['HTTP_SEC_WEBSOCKET_KEY'], env.get('HTTP_ORIGIN', ''))

#       print "enter websockets..."

        #on user's first connection, subscribe to his own uid

        websocket_fd = uwsgi.connection_fd()
        redis_fd = None
        r_ps = r.pubsub()
        my_uid = None

        print 'websocket_fd=', websocket_fd
        
        while True:
            gevent.sleep(0.5) #allow other greenlets to run
            print 'after gevent sleep 1 second ...'

            # wait max 4 seconds to allow ping to be sent
            if redis_fd:
                ready = gevent.select.select([websocket_fd, redis_fd], [], [], 4.0)
            else:
                ready = gevent.select.select([websocket_fd], [], [], 4.0)

            print 'ready=', ready

            # send ping on timeout
            if not ready or not ready[0]:
                print 'Not ready, no text coming ?'
                uwsgi.websocket_recv_nb()
                #If user left, uwsgi/gevent/ws will fail, 
                #this greenlet will auto ended. 
                #
                #Relative websocket_fd, redis_fd will be auto removed ?
                #
                #Anyway, don't use: try ... except ... to catch the IOError,
                #or greenlet will never end
#               continue

            for fd in ready[0]:
                if fd == websocket_fd:
                    print 'websocket_fd=', fd


                    #Don't try to catch IOError, or this greenlet can't end
                    w_msg = uwsgi.websocket_recv_nb() #websocket_msg

                    if not w_msg: #No message from user
                        continue

                    # logging.debug ('websocket_msg =%s' % w_msg)
                    w_msg_dict = dict(urlparse.parse_qsl(w_msg))
                    
                    channel_list = [c for c in w_msg_dict['channels'].split(',') if c]
                    if 'api' in w_msg_dict:
                        if w_msg_dict['api'] == 'sub' and 'channels' in w_msg_dict:
                            r_ps.subscribe(channel_list) 
                            redis_fd = r_ps.connection._sock.fileno()
                        elif w_msg_dict['api'] == 'unsub' and 'channels' in w_msg_dict:
                            r_ps.unsubscribe(channel_list) 
                            redis_fd = r_ps.connection._sock.fileno()
                        elif w_msg_dict['api'] == 'numsub' and 'channels' in w_msg_dict:
                            result = r_ps.numsub(channel_list) 
                        elif w_msg_dict['api'] == 'pub':
                            #print 'user/client sent w_msg to websocket:', w_msg
                            # if 'msg' in w_msg_dict:
                            #     r.publish(w_msg_dict['uid'], w_msg_dict['msg']) 
                            # elif 'content' in w_msg_dict:   #older testing key
                            #     r.publish(w_msg_dict['uid'], 
                            #             w_msg_dict['content'])
                            channel_list = [c for c in w_msg_dict['channels'].split(',') if c]
                            if w_msg_dict.get("content"):
                                for channel in channel_list:
                                    r.publish(channel,w_msg_dict['content'])
                    else:
                        print 'error, no api in w_msg_dict:', w_msg_dict
                        #print 'user/client sent w_msg to websocket:', w_msg
                        #print 'we forward it to redis'
                        #r.publish(w_msg['message'])

                elif fd == redis_fd:
                    w_msg_dict = dict(urlparse.parse_qsl(w_msg))
                    channel_list = [c for c in w_msg_dict['channels'].split(',') if c]
                    # for i in len(channel_list):
                    channel_num = len(channel_list)
                    while channel_num:
                        r_msg = next(r_ps.listen())  #redis_msg
                        if r_msg:
                            channel_num -= 1
                            uwsgi.websocket_send(json.dumps(r_msg))
        
            timeAgo = time.time() - 10*60 #10 minutes ago
            for uid in active_users:
                if active_users[uid] < timeAgo:
                    del(active_users[uid])

            print '\nThis server, total active users in 10 min:', len(active_users)
            print 'This server, total active UIDs in 10 min:', active_users.keys()


