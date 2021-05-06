import sys
sys.stdin=open("input.txt", "r")

n=int(input())
a=list(map(int, input().split()))

count=0
sum=0

for i in range(n):
    if a[i]==1:
        count=count+1
        sum=sum+count
    else:
        count=0

print(sum)
