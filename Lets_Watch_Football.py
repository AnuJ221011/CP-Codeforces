a,b,c=map(int,input().split())
temp=0
for i in range(1,((c*a)//b+1)):
    if a*c>=((b*i)+(b*c)):
        temp=i
    else:
        break
if ((b*temp)+(b*c))==a*c:
    print(temp)
else:
    print(temp+1)
