t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    print(min((abs(a-b)+abs(b-c)),(abs(a-c)+abs(c-b)),(abs(b-a)+abs(c-a))))