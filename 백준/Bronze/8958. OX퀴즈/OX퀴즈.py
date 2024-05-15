T=int(input())

for i in range(T):
    a=0
    A=str(input())
    c=[]
    for b in A:
        if b == 'O':
            a += 1
        else:
            a=0
        c.append(a)

    print(sum(c))