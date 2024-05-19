X=int(input())
N=int(input())
price=0
for i in range(N):
    a,b=list(map(int,input().split()))
    price += (a*b)
    b=i+1

if X==price and N==b:
    print('Yes')
else:
    print('No')