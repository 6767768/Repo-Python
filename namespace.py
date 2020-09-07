import sys
print("Name of module sys: ", sys.__name__)
print("Name of present module: ", __name__)


# Only when present module is executed, print Private info,
# If present module is used as external source, nothing printed.
if __name__ == "__main__":
    print("Priavte info")


x = 1
def foo():
    y = 2
    print(globals())
    print(locals())

foo()


# namespace can be sorted as four classes, presented in dictionary forms. 
# local namespace: locals()
# global namespace: globals()
# build-in namespace
# namespace packages


def make_average():
    count = 0
    total = 0
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager

averager = make_average()
print(averager(10))
print(averager(11))


# nonlocal 使得内部函数可以修改外部函数的变量，但是并不进行回收操作，该函数成为闭包


def make_averagee():
    count = 0
    def ss(new_value):
        # nonlocal count
        count += new_value
        return count

    return ss

a = make_averagee()
print(a(10))














