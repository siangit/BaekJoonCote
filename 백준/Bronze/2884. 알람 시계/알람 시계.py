H,M=map(int,input().split())

if M < 45:
    M = 60 - (45-M)
    if H == 0:
        H=24-1
    else:
        H=H-1
else:
    M = M-45
print(f'{H} {M}')
