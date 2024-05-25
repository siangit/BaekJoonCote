n=int(input())

for i in range(n):
    answer=""
    x=input().split()
    for _ in range(len(x)):
        answer += x.pop()+" "
    print(f'Case #{i+1}: {answer}')