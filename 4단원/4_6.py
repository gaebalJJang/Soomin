import sys
sys.stdin=open("input.txt", "r")

#변수
n=int(input())
body=[]

for i in range(n):
    a, b=map(int, input().split())
    body.append((a, b))
    
body.sort(reverse=True)
largest=0
count=0

for x, y in body:
    if y>largest:
        largest=y
        count+=1
        
print(count)
