n=42
list=[]
for _ in range(10):
    number = int(input())%42
    if number not in list:
        list.append(number)

print(len(list))
