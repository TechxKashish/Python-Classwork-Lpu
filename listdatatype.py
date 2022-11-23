# l=[2,3,4,5]
# print(type(l),len(l))
# a=3
# print(id(a))
# a=10
# print(id(a))

# numbers=[]
# list_2 = list()
# print(len(numbers),len(list_2))
# list_2.append(1)
# list_2.append(2)
# print(list_2)
# list_1 = list_2
# print(list_1)
# print(list_1[1])

# you have a task to find an element in list if it is not there then add it
# list1 = [2,3,56,45,89,10]
# var=int(input('enter a number'))
# if var in list1:
#     print(list1.index(var))
# else:
#     list1.append(var)
#     print(list1)


# find is there element or not 
list1=[2,3,5,67,89]
var= int(input('enter a number'))
n=var not in list1
# print(n)

str1="lovely professional university"
print("lovely"in str1)
listk=[91,28,43,49,75,96,17]
list2=[0,9,8,7]
# print(listk[1:5])
'''methods'''
#sort
# listk.sort()
print(listk)
#reverse
# listk.reverse()
# print(listk)
# append add element at last
# listk.append(3)
# insert
listk.insert(3,45)
print(listk)
# listk.pop(3)
print(listk)
listk[2]=listk[2]+2
print(listk)
# remove
# listk.remove(45)
print(listk)
print(listk.count(45))