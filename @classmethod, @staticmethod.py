class A:
    num = "aaa"

    def func1(self):
        print("func1")
        print(self)

    @classmethod
    def fun2(cls):
        print("func2")
        print(cls)
        print(cls.num)

        cls().func1()

    def func3():
        print("func3")
        print(A.num)


##A.func1() 这样调用是会报错：
##因为func1()调用时需要默认传递实例化类后的地址id参数，
##如果不实例化类是无法调用的
