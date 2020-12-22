# 数値で各変数に代入
n, a, b = map(int, input().split())
ans = 0
# 1 ～ n でループ
for i in range(1, n + 1):
    s = str(i)
    digit_all = sum(list(map(int, s)))
    if a <= digit_all <= b:
        ans += i
print(ans)