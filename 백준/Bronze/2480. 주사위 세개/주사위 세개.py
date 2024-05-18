dice=input().split()

if dice[0] == dice[1]:
    if dice[0] ==dice[2]:
        answer=10000+(int(dice[0])*1000)
    else:
        answer=1000+(int(dice[0])*100)
elif dice[0] == dice[2]:
    if dice[0] ==dice[1]:
        answer=10000+(int(dice[0])*1000)
    else:
        answer=1000+(int(dice[0])*100)
elif dice[1] == dice[2]:
    if dice[0] ==dice[1]:
        answer=10000+(int(dice[1])*1000)
    else:
        answer=1000+(int(dice[1])*100)
else:
    answer=int(max(dice))*100

print(answer)
