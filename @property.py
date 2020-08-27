class Person(object):
    # __func__ is defined as private functions
    # __var is defined as private variables.
    # _var is defined as public variables, but accessing is not recommended
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age_fun(self, value):
        # isinstance judges the type of the variable
        if not isinstance(value, int):
            raise ValueError("sss")

        if value < 0 or value > 100:
            raise ValueError("aaa")

        self.__age = value

    def print_info(self):
        print("%s:%s"%(self.__name, self.__age))


# 实际上这个__age变量和class内部的__age变量不是一个变量！
# 内部的__age变量已经被Python解释器自动改成了_Person_age，而外部代码给p新增了一个__age变量。 所以调用 get_age_fun输出的是初始值

class Person1(object):
    # __func__ is defined as private functions
    # __var is defined as private variables.
    # _var is defined as public variables, but accessing is not recommended
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    def get_age(self):
        return self._age

    def set_age_fun(self, value):
        # isinstance judges the type of the variable
        if not isinstance(value, int):
            raise ValueError("sss")

        if value < 0 or value > 100:
            raise ValueError("aaa")

        self._age = value

    def print_info(self):
        print("%s:%s"%(self.__name, self._age))



# @property装饰器就是负责把一个方法变成属性调用.

class Person2(object):
    # __func__ is defined as private functions
    # __var is defined as private variables.
    # _var is defined as public variables, but accessing is not recommended
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age_fun(self, value):
        # isinstance judges the type of the variable
        if not isinstance(value, int):
            raise ValueError("sss")

        if value < 0 or value > 100:
            raise ValueError("aaa")

        self.__age = value

    def print_info(self):
        print("%s:%s"%(self.__name, self.__age))


class Person3(object):
    # __func__ is defined as private functions
    # __var is defined as private variables.
    # _var is defined as public variables, but accessing is not recommended
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age_fun(self, value):
        # isinstance judges the type of the variable
        if not isinstance(value, int):
            raise ValueError("sss")

        if value < 0 or value > 100:
            raise ValueError("aaa")

        self.__age = value


    @get_age.deleter
    def get_age(self):
        self.__age = 0
        # del self.__age

    def print_info(self):
        print("%s:%s"%(self.__name, self.__age))

p = Person3('aaa', 20)
p.set_age_fun = 35
print(p.get_age)

del p.get_age
print(p.get_age)












