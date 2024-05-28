n,m=map(int,input().split())
list=[i for i in range(1,n+1)]

for _ in range(0,m):
    x,y=map(int,input().split())
    extra = list[x-1]
    list[x-1]=list[y-1]
    list[y-1]=extra

for i in range(n):
    print(list[i],end=' ')