##class Score:
##    def __init__(self, default = 0):
##        self._score = default
##    def __set__(self, instance, value):
##        if not isinstance(value, int):
##            raise TypeError("Score must be integer")
##        if not 0 <=value <= 100:
##            raise ValueError("Invalid value")
##
##        self._score = value
##
##    def __get__(self, instance, owner):
##        return self._score
##
##    def __delete__(self):
##        del self._score
##
##class Student:
##    
##    math = Score(0)
##    chinese = Score(0)
##    english = Score(0)
##
##    def __init__(self, name, math, chinese, english):
##        self.name = name
##        self.math = math
##        self.chinese = chinese
##        self.english = english
##
##    def __repr__(self):
##        return "{},{},{}".format(self.math, self.chinese, self,english)
##
##    





class DataDes:
    def __init__(self, default = 0):
        self._score = default

    def __set__(self, instance, value):
        self._score = value

    def __get__(self, instance, value):
        print("DataDes __get__")
        return self._score

class NoDataDes:
    def __init__(self, default = 0):
        self._score = default

    def __get__(self, instance, owner):
        print("NoDataDes __get__")
        return self._score


##需要注意的是，math 是数据描述符，
##而 chinese 是非数据描述符。从下面的验证中，
##可以看出，当实例属性和数据描述符同名时，
##会优先访问数据描述符（如下面的math），
##而当实例属性和非数据描述符同名时，
##会优先访问实例属性（__getattribute__）
class Student:
    math = DataDes(0)
    chinese = NoDataDes(0)

    def __init__(self, name, math, chinese):
        self.name = name
        self.math = math
        self.chinese = chinese

    def __getattribute__(self, item):
        print("__getattribute__")
        return super().__getattribute__(item)

    def __repr__(self):
        return "{},{},{}".format(self.math, self.chinese, self,english)

        




























