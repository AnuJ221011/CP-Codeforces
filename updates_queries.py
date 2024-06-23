t=int(input())

for _ in range(t):
    n,m=map(int,input().split())
    s = list(input())
    indices=list(map(int,input().split()))
    indices=[i-1 for i in indices]
    c=sorted(list(input()))
    sorted_indices = sorted(indices)
    check=['false']*n
    j=0
    for i in sorted_indices:
        if check[i] == 'false':
            s[i] = c[j]
            check[i] = 'true'
            j+=1

    print(''.join(s))