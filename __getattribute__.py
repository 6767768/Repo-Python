class A:
    def __getattribute__(self, name):
        print("in A")
        return super().__getattribute__(name)

class B(A):
    def spam(self):
        print("spam")


#b= B()

##当在命令行输入b.spam(，甚至括号还没有输入完整的时候，
##              就已经触发了__getattribute__。
##              可见，当实例在查找任何属性的时候
##              （注意是实例，这是另一个知识点，后面再详谈），
##              都会触发__getattribute__方法。


def log_attr(cls):
    cls_getattribute = cls.__getattribute__
    def new_getattribute(self, name):
        print("catch name")
        return cls_getattribute(self, name)

    cls.__getattribute__ = new_getattribute

    return cls

@log_attr
class C:
    def __init__(self, x):
        self.x = x

    def spam(self):
        print("spam")


##特殊的方法，如__len__，__str__等等操作符重载方法，当隐式调用的时候，
##在python3中会直接在类的命名空间中查找，因此是不会触发__getattribute__的


##but，当直接显示调用的时候，python不会将其当作啥特殊方法，
##仍然会从实例的命名空间查找
class A:
    def __len__(self):
        return 42

    def __getattribute__(self, name):
        print("ssss")
        return super().__getattribute__(name)

    




















