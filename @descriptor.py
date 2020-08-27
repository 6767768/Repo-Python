class Score:
    def __init__(self, default = 0):
        self._score = default
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Score must be integer")
        if not 0 <=value <= 100:
            raise ValueError("Invalid value")

        self._score = value

    def __get__(self, instance, owner):
        return self._score

    def __delete__(self):
        del self._score

class Student:
    
    math = Score(0)
    chinese = Score(0)
    english = Score(0)

    def __init__(self, name, math, chinese, english):
        self.name = name
        self.math = math
        self.chinese = chinese
        self.english = english

    def __repr__(self):
        return "{},{},{}".format(self.math, self.chinese, self,english)

    
