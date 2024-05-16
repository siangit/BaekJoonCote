x,y=map(list,input().split())
x=''.join(reversed(x))
y=''.join(reversed(y))
if x>y:
    print(x)
else:
    print(y)