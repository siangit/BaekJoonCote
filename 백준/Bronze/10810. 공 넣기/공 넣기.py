n,m=map(int,input().split())
list=[0]*(n+1)

for _ in range(0,m):
    x,y,z=map(int,input().split())
    for i in range(x,y+1):
        list[i]=z

for i in range(1,n+1):
    print(list[i],end=' ')