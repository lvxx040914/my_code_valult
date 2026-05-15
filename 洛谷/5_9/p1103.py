n,k = map(int,input().split())
lis = []
for _ in range(n):
    i,j = map(int,input().split())
    lis.append((i,j))
lis.sort(key = lambda x:x[1])
res = 0
for i in range(n-1):
    res += (lis[i+1][1] - lis[i][1])
print(res)