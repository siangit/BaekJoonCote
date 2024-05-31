import sys 
sys.setrecursionlimit(10006)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def non_zero(n):
    figureout = factorial(n)
    while figureout % 10 == 0:
        figureout //= 10
    return figureout % 10

t = int(input())
for _ in range(t):
    n = int(input())
    print(non_zero(n))