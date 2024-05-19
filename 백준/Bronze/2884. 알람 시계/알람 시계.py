H,M=map(int,input().split())


if 45 <= M:
    H == H
    M = M-45
elif M < 45:
    M = M+60-45
    if H < 0:
        H==abs(H)
        H=24-H
    elif H == 0:
        H = 23
    else:
        H = H-1


print(f'{H} {M}')