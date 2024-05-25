n=int(input())
stack=[]

for _ in range(n):
    h = int(input())

    if not stack:
        stack.append(h)
        continue

    while True:
        if not stack:
            break
        if stack[-1] <= h:
            stack.pop()
        else:
            break

    stack.append(h)

print(len(stack))