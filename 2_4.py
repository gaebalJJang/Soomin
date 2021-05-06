import sys 
sys.stdin=open("input.txt", "rt")

n=int(input())
a=list(map(int, input().split()))

avg=sum(a)/n
avg=avg + 0.5
avg=int(avg)

min=2147000000

for idx, x in enumerate(a):
    temp = abs(x-avg)
    if temp<min:
        min=temp
        score=x
        res=idx+1
    elif temp==min:
        if x>score:
            score=x
            res=idx+1
print(avg, res)
