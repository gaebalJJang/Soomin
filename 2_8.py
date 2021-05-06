import sys 
sys.stdin=open("input.txt", "r")

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x):
        if x%i==0:
            return False
    else:
        return True


n=int(input())
a=list(map(int, input().split()))

for x in a:
    tmp=reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
