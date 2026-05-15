n = int(input())
a = list(map(int,input().split()))
sum1 = 0
for ai in a:
    sum1 += ai**2
sum2 = sum(a)
print((sum2**2 - sum1)//2)