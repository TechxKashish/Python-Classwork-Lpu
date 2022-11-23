# list1=[2,3,4,5,6]
# list2=[3,6,2,1]
# list3=[]
# for item1 in list1:
#     for item2 in list2:
#         if item1==item2:
#            list3.append(item1)
#            break 
#     print(list3)

# list1=[2,3,4,5,6]
# list2=[3,6,2,1]
# list3=list1
# i=0
# for item1 in list1:
#     for item2 in list2:
#         if item1==item2:
#            list3[i]=item1+1
#     i=i+1      
#     print(list3)

# list1=[2,3,4,5,6]
# list2=[3,6,2,1]
# for i in range(len(list1)):
#     for j in range(len(list2)):
#         if list1[i]==list2[j]:
#             list1[i]=list1[i]+1
#             break
# print(list1)

# list1=['p','Y','t','O','n']
# for i in range(len(list1)):
#     if i==0 and list1[i]>='a' and list1[i]<='z':
#         list1[i]=chr(ord(list1[i])-32)
#     else:
#         if list1[i]>='A' and list1[i]<='Z':
#             list1[i]=chr(ord(list1[i]+32))
# print(list1)

# list1=list()
# for i in range(2):
#     list1.append([])
#     for j in range(3):
#         list1[i].append(0)
# print(list1)list1=list()

list1=list()
for i in range(2):
    list1.append([])
    for j in range(3):
        var=int(input('var: '))
        list1[i].append(var)
print(list1)
list1[1][2]=10
total=0
for i in range(len(list1)):
    for j in range(len(list1[i])):
        total=total+list1[i][j]
        print(list1[i][j],end=' ')
    print()





