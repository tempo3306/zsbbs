# def use(level):
#     def usebar(func):
#         def wrapper(*args,**kwargs):
#             if level>0:
#                 print(*args)
#             return func(*args,**kwargs)
#         return wrapper
#     return usebar
# @use(level=0)
# def bar(x,y):
#     print(x+y)
#
# # bar = usebar(bar)
# bar(1,2)
class use():
    def __init__(self,func):
        self._func = func

    def __call__(self):
        print ("fdf")
        self._func()
        print("over")

@use
def bar():
    print("fdsfggg")
bar()

