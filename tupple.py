# t=1,2,3,4
# t1=(1,2,3,4)
# print(t,t1,sep="\n")
# print(type(t))
# l=[2,3,4,5]
# t2=tuple(l)
# t2=list(t2)
# for i in range(len(t2)):
#     t2[i]=t2[i]+1
# t2=tuple(t2)
# print(t2)


# data=input('data')
# #generate a list from input
# if ',' in data:
#     data=data.split(',')
# elif ' ' in data:
#     data=data.split()
# #convert the list to a tuple
# data=tuple(data)45
# #taking index as input
# index=int(input("index: "))
# if index<len(data) and index>=-len(data):
#     print('the tuple is:',data)
#     print('element:',data[index])
# else:
#     print('invalid index')




data=input('data')
if ',' in data:
    data=data.split(',')
elif ' ' in data:
    data=data.split()
data=tuple(data)
index=int(input("index: "))
if index!=-1:
    if index<len(data) and index>=-len(data):
        data=data[0:index]+data[index+1:]
        print('tuple is:',data)
    else:
        print('invalid index')
else:
    print("tuple is:",data[:index])
