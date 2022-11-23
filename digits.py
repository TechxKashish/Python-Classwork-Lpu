while True:
    n=int(input())
    i=s=0
    if n<0:
        print('enter again')
    else:
        while True:
            d=int(n%10)
            n=n/10
            s=s+d
            if d==0:
                break
    print('sum: ',s)

    