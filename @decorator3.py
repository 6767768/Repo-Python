import random
import wrapt

'''
def provide_number(min_num, max_num):

"""装饰器：随机生成一个在 [min_num, max_num] 范围的整数，追加为函数的第一个位置参数
    """
    
    def wrapper(func):
        def decorated(*args, **kwargs):
            num = random.randint(min_num, max_num)

            # 将 num 作为第一个参数追加后调用函数
            return func(num, *args, **kwargs)
        return decorated
    return wrapper

# 嵌套层级深、无法在类方法上使用
@provide_number(1, 100)
def print_random_number(num):
    print(num)

print_random_number()

'''

def provide_number(min_num, max_num):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):

#         参数含义：       
# - wrapped：被装饰的函数或类方法
# - instance：
#   - 如果被装饰者为普通类方法，该值为类实例
#   - 如果被装饰者为 classmethod 类方法，该值为类
#   - 如果被装饰者为类/函数/静态方法，该值为 None
# - args：调用时的位置参数（注意没有 * 符号）
# - kwargs：调用时的关键字参数（注意没有 ** 符号）
        
        num = random.randint(min_num, max_num)

        args = (num, ) + args

        return wrapped(*args, **kwargs)

    return wrapper








