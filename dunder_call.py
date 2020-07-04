class A:

    def __init__(self,arg1):
        print(f"Got {arg1} at the time of constructer")

    def __call__(self,arg2):
        print(f"Got {arg2} from object and can be called with .attr")

    def fun(self,arg3):
        print(f"Got {arg3} by calling fun method ")


a = A('init')                # for __init__
a('call')                   # for __call__
a.fun('fun')                # for fun
