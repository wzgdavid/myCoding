#!/usr/bin/python
#coding=utf8
# https://github.com/unbit/uwsgi/blob/master/tests/wss_chat.py
#

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

def application(env, start_response):
    print '\nPATH_INFO=', env['PATH_INFO']

    ws_scheme = 'ws'
    if 'HTTPS' in env or env['wsgi.url_scheme'] == 'https':
        ws_scheme = 'wss'

    if env['PATH_INFO'] == '/':
        start_response('200 OK', [('Content-Type','text/html')])
        return """
    <html>
      <head>
          <script language="Javascript">
            var s = new WebSocket("%s://localhost:9123/ws/");

            s.onopen = function() {
              alert("Websocket connected !!!");
            };

            s.onmessage = function(e) {
        var bb = document.getElementById('blackboard')
        var html = bb.innerHTML;
        bb.innerHTML = html + '<br/>' + e.data;
            };

        s.onerror = function(e) {
            alert(e);
        }

        s.onclose = function(e) {
        alert("connection closed");
        }

            function new_room() {   //i.e. new websocket
          var uid = document.getElementById('uid').value;
              s.send("api=sub&channels=" + uid + "&uid=" + uid);
              alert("New room/channel: " + uid + ", connected.");
            };


            function send_msg() {
              var uid = document.getElementById('uid').value;
          var value = document.getElementById('msg').value;
              s.send("api=pub&uid=" + uid + "&msg=" + value);
            }

            function listen_uids() {
              var friend_uids = document.getElementById('friend_uids').value;
              var uid = document.getElementById('uid').value;
              s.send("api=sub&channels=" + friend_uids + "&uid=" + uid);
              alert("Added friend's rooms/channels/uids: " + friend_uids);
            }

            function unsubscribe_uids() {
              var friend_uids = document.getElementById('friend_uids').value;
              var uid = document.getElementById('uid').value;
              s.send("api=unsub&channels=" + friend_uids + "&uid=" + uid);
              alert("Exited/Unsubscribed friend's rooms/channels/uids: " + friend_uids);
            }

            function numsub() {
              var friend_uids = document.getElementById('friend_uids').value;
              var uid = document.getElementById('uid').value;
              result=s.send("api=numsub&channels=" + friend_uids + "&uid=" + uid);
              alert("Count/NumSub results:" + results);
            }
          </script>
     </head>
    <body>
        <h1>WebSocket</h1>
        <p>Only room owner can speak, friends listen only. Room # is same as user's UID.

        <p>
        UID: <input type="text" id="uid" value=""/>
        <input type="button" value="New room/channel named my UID" onClick="new_room();"/>
        <div style='color:gray'>(i.e. subscribe to my own room, so that I can speak.)</div>


        <p>Listen to Friend/Room UIDs: <input type="text" id="friend_uids" value=","/>
        <input type="button" value="Listen Friends' Channel/Room" onClick="listen_uids();"/>
        <br/>
        <input type="button" value="Exit/Unsubscribe Friends' Channel/Room" onClick="unsubscribe_uids();"/>
        <div style='color:gray'>* Subscribe to nobody, will close connection.
        <br/>
        <br/>

        <input type="button" value="Count/NumSub Total Subscribers" onClick="numsub();" disabled/>
        <br/>* PubSub.NumSub only works for redis 2.8+, but newest redis-py binding (2014/Apr) still doesn't support yet.
        </div>


        <p>
        MSG: <input type="text" id="msg" value="Help! Emergency!"/>
        
        <br/>
        <input type="button" value="Speak in my room/channel" onClick="send_msg();"/>

    <div id="blackboard" style="width:640px;height:480px;background-color:black;color:white;border: solid 2px red;overflow:auto">
    </div>

    </body>
    </html>
        """ % ws_scheme #, env['HTTP_HOST'])


    elif env['PATH_INFO'] == '/favicon.ico':
        return ""

