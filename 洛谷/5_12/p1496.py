n = int(input())
lis = []
for _ in range(n):
    a,b = map(int,input().split())
    lis.append((a,b))
lis.sort()
total = 0
cur_start,cur_end = lis[0][0],lis[0][1]
for i in range(1,n):
    if cur_end < lis[i][0]:
        total += cur_end - cur_start
        cur_start,cur_end = lis[i][0],lis[i][1]
    else:
        cur_end = max(lis[i][1],cur_end)
total += cur_end - cur_start
print(total)
        