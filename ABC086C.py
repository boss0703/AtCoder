# t x y
# 移動可能距離を超過してないかチェック t >= |x| + |y| 絶対値abs()
# 全部合計して偶数ならYES
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
ans = ''
for i in range(0, n):
    ans = 'No'
    if i == 0:
        if l[i][0] >= (l[i][1] + l[i][2]):
            if sum(l[i]) % 2 == 0:
                ans = 'Yes'
    else:
        if l[i][0] - l[i-1][0] >= abs(l[i][1] - l[i-1][1]) + abs(l[i][2] - l[i - 1][2]):
            if (l[i][0] - l[i-1][0] + l[i][1] - l[i-1][1] + abs(l[i][2] - l[i - 1][2])) % 2 == 0:
                ans = 'Yes'
    if ans == 'No':
        break
print(ans)