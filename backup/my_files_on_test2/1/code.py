class A(object):
    def __init__(self,param):
        print("__init__")
        print(param)
    def __new__(self,param):
        print("__new__")
        print(param)

A('yes')
