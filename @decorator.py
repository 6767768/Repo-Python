from functools import wraps
##def decorator_name(f):
##    #@wraps(f)
##    def decorated(*args, **kwargs):
##        if not can_run:
##            return "Function will not run"
##        return f(*args, **kwargs)
##    return decorated
## 
##@decorator_name
##def func():
##    return("Function is running")
## 
##can_run = True
##print(func())
### Output: Function is running
## 
##can_run = False
##print(func())
### Output: Function will not run
##
##print(func.__name__)
##print(func.__doc__)


##@wraps接受一个函数来进行装饰，
##并加入了复制函数名称、注释文档、参数列表等等的功能。
##这可以让我们在装饰器里面访问在装饰之前的函数的属性。

def a_new_decorator(a_func):
    @wraps(a_func)
    def WrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")
    return WrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("I am the function which needs some decoration to "
          "remove my foul smell")




def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开logfile，并写入内容
            with open(logfile, 'a') as opened_file:
                # 现在将日志打到指定的logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator
 
@logit()
def myfunc1():
    pass





















