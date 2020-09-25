'''
list1 = [1,2,3,4]
list2 = [5,6,7,8]

for (x,y) in zip(list1,list2):
    print (x,y, "==",x+y)
'''

a = [1,2,3]
b = [4,5,6]

zipped = zip(a, b)

print(list(zip(*zipped)))
