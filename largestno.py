a,b,c=10,23,67
if a>b and a>c:
    print('a is largest')
elif b>c:
    if b==a:
        print('b and a is largest and equal')
    else:
        print('b is largest')
else:
    if a==b and a==c:
        print('all are same')
    elif c==a:
     print('c and a is equal and largest')
    elif c==b:
     print('c and b is equal and largest')
    else:
     print('c is largest')