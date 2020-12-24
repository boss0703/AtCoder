h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
# 二次元配列の最小値
m = 100
for aline in a:
    for i in aline:
        if m > i:
            m = i
ans = 0
for aline in a:
    for i in aline:
        if i > m:
            ans += i - m
print(ans)
