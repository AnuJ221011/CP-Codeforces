import math
t=int(input())
for _ in range(t):
    n=int(input())
    temp=2
    count=0
    i=0
    check=0
    while n>1:
        if temp<=n:
            check=temp
            temp=temp+5+3*i
            i+=1
        else:
            count+=1
            i=0
            n=n-check
            temp=2
    print(count)
