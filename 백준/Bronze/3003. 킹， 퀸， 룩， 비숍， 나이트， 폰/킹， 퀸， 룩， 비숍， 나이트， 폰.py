[k,q,l,b,n,p]=map(int,input().split())
# kk,qq,ll,bb,nn,pp=(1,1,2,2,2,8)
chess=[1,1,2,2,2,8]
result=[]
for i in range(len(chess)):
    result.append(chess[i]-[k,q,l,b,n,p][i])

k,q,l,b,n,p=result
answer =f'{k} {q} {l} {b} {n} {p}'
print(answer)