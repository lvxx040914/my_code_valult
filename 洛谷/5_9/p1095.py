M, S, T = map(int, input().split())

flash = [0] * (T + 1)

magic = M

for i in range(1, T + 1):

    # 闪烁 / 休息恢复
    if magic >= 10:
        flash[i] = flash[i - 1] + 60
        magic -= 10
    else:
        flash[i] = flash[i - 1]
        magic += 4

ans = 0

for i in range(1, T + 1):

    # 跑步
    ans += 17

    # 和闪烁取最大
    ans = max(ans, flash[i])

    if ans >= S:
        print("Yes")
        print(i)
        break

else:
    print("No")
    print(ans)