T=9
result=[]
for i in range(T):
    x=int(input())
    result.append(x)

answer=max(result)
indexofanswer=int(result.index(answer))+1
print(answer)
print(indexofanswer)