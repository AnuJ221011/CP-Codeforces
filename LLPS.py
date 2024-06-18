s=input()
s=sorted(s,reverse=True)
res=""
res+=s[0]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        res+=s[i]
    else:
        break
print(res)
