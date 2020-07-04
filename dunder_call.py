class A:

    def __init__(self, arg1):
        print("Got {} at the time of constructer".format(arg1))

    def __call__(self, arg2):
        print("Got {} from object and can be called with .attr".format(arg2))

    def fun(self, arg3):
        print("Got {} by calling fun method ".format(arg3
        	))


a = A('init')                # for __init__
a('call')                   # for __call__
a.fun('fun')                # for fun
