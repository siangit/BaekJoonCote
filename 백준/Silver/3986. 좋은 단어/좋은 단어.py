n = int(input())
goodword = 0

for _ in range(n):
    stack=[]
    word=list(input())
    for i in word:
        if len(stack) == 0:
            stack.append(i)
        elif stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)
    
    if len(stack) <= 0:
        goodword += 1

print(goodword)