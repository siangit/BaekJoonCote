word = input()
n = int(input())
answer = 0

for i in range(n):
    ring = input()*2
    if word in ring:
        answer += 1

print(answer)