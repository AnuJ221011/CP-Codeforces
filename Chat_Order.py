n = int(input().strip())
li = [input().strip() for _ in range(n)]
dic={}
for i in reversed(li):
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1

for keys in dic:
    print(keys)

