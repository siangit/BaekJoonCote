from sys import stdin

n=int(input())
stack=[]

for _ in range(n):
    h = int(stdin.readline())

    if not stack:
        stack.append(h)
        continue

    while stack and stack[-1] <= h:
        stack.pop()

    stack.append(h)

print(len(stack))