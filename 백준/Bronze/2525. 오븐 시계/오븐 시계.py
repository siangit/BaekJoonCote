A,B=map(int,input().split())
C=int(input())

x=B+C
H,M=divmod(x,60)

H=H+A
while M >= 60:
    B=M-60
    A +=1
else:
    A==A
    M==M

if H >= 24:
    H = H-24
else:
    H==H

print(f'{H} {M}')