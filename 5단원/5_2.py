import sys
sys.stdin=open("input.txt", "r")

#변수 선언
s = input()
stack = []
count = 0

for i in range(len(s)):
    if s[i]=='(':
        stack.append(s[i])
    else:
        stack.pop()
        if s[i-1]=='(':
            count+=len(stack)
        else:
            count+=1
print(count)
