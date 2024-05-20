star='*'
N=int(input())
result=' '
for i in range(N):
    answer=(result*(N-(i+1))+(star*(i+1)))
    print(answer)

    