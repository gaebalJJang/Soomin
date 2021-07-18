import sys
from collections import deque

sys.stdin=open("input.txt", "r")

#변수 선언
n, m=map(int, input().split())
Q=[(pos, val) for pos, val in enumerate(list(map(int, input().split())))]
Q=deque(Q)
count = 0

while True:
    cur = Q.popleft()
    if any(cur[1]<x[1] for x in Q):
        Q.append(cur)
    else:
        count+=1
        if cur[0]==m:
            print(count)
            break
