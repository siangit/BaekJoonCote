n,m=map(int,input().split())
list=[i for i in range(1,n+1)]


for _ in range(m):
    x,y=map(int,input().split())
    extra=list[x-1:y]
    extra.reverse()
    list[x-1:y] = extra

for i in range(n):
    print(list[i], end=' ')