# # mydic={"game":"chess","dish":"chicken","place":"home"}
# # print(mydic.get('game'))
# # print(mydic.get('dish'))
# # print(mydic.get('place'))
# # mydic['game']="cricket"
# # print(mydic['game'])

# keys=input('keys: ')
# keys=keys.split(',')
# values=input('values: ').split(',')
# # d=dict()
# d=dict(zip(keys,values))
# print(d)
# d2=dict()
# if len(keys)==len(values):
#     for i in range(0,len(keys)):
#         d2[keys[i]]=values[i]
#     print(sorted(d2.items()))
# else:
#     print('length should be equal')

# print(d2[1])
# print(d2.get(1))

# keys=input',')
# d=dict(zip(keys,values))
# d=sorted(d)
# for key,value in d:
#     print(key,value)

# d={1:'a',2:'4',3:'t'}
# print(d.pop(1))
# print(d.popitem)
# print(d)

keys=input('keys: ')
keys=keys.split(',')
values=input('data2: ').split(',')
keys=[int(key)for key in keys]
values=[int(value) for value in values]
d=dict(zip(keys,values))
min=d[keys[0]]
max=min
for key,value in d.items():
    if value>max:
        max=value
    if value<min:
        min=value
print('max:',max)
print('min:',min)
