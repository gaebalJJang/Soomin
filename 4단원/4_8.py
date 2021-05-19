import sys
from collections import deque
sys.stdin=open("input.txt", "r")

#변수
n, limit=map(int, input().split())
p=list(map(int, input().split()))
p.sort()
p=deque(p)
count=0

while p:
    if len(p)==1:
        count+=1
        break
    if p[0]+p[-1]>limit:
        p.pop()
        count+=1
    else:
        p.popleft()
        p.pop()
        count+=1
        
print(count)

