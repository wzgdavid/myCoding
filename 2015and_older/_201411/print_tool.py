# encoding: utf-8

import json


def pprint(obj):
    '''清晰显示dict'''
    class MyEncoder (json.JSONEncoder):
        def default(self, o):
            try:
                iterable = iter(o)
            except TypeError:
                pass
            else:
                return list(iterable)
            try:
                return json.JSONEncoder.default(self, o)
            except TypeError:
                return str(o)
    
    orig = json.dumps(obj,
                      indent=4,
                      sort_keys=True,
                      skipkeys=True,
                      cls=MyEncoder)
    print eval("u'''%s'''" % orig).encode('utf-8')

#d = 1,{'one': 1, 'two': False, 'three': {'one': 1, 'two': 2, 'three': 3}}
#pprint(d)
