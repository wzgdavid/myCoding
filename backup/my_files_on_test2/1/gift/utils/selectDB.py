#codin: utf-8
import pymongo

conf = {
    'cn': {
        'online': {
            'ip': '10.161.177.73',
            'port': 27017,
            'db': 'cnmaxstrikedb1a',
            'user': 'cnmaxstrikeuser1aocdata',
            'pwd': 'cnmaxstrikeuPwD1&aooCdata',
        },
        'log': {
            'ip': '10.161.177.73',
            'port': 27017,
            'db': 'logcnmaxstrikedb1a',
            'user': 'logcnmaxstrikeuser1aocdata',
            'pwd': 'logcnmaxstrikeuPW1oa&oCdata',
        },
    },

    'tw': {
        'online': {
            'ip': '54.238.211.119',
            'port': 27017,
            'db': 'awsmaxstrikedb1a',
            'user': 'awsmaxstrikeuse1aocdata',
            'pwd': 'awsmaxstrikeupwD1&aooCdata',
        },
        'log': {
            'ip': '54.238.211.119',
            'port': 27017,
            'db': 'logawsmaxstrikedb1a',
            'user': 'logawsmaxstrikeuser1aOcdata',
            'pwd': 'logawsmaxstrikeuPw2oa&oCdata',
        },
    },    
}

def db(serve, base):
    db_conf = conf[serve][base]
    conn = pymongo.Connection(db_conf['ip'], db_conf['port'])
    this_db = conn[db_conf['db']]
    this_db.authenticate(db_conf['user'], db_conf['pwd'])

    return this_db
