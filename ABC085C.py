n, y = map(int, input().split())
# お札の枚数ループ(iは10000円札の枚数)
for i in range(n + 1):
    # jは5000円札の枚数
    for j in range(n - i + 1):
        # お札の全体の枚数はnなので1000円札は引いた残りになる
        if i * 10000 + j * 5000 + (n - i - j) * 1000 == y:
            print(i, j, n - i - j)
            exit()
print(-1, -1, -1)