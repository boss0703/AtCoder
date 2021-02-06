h, w = map(int, input().split())
s = list(list())
for k in range(h):
    s.append(list(input()))
# #からみて上下左右を見て#がなければ4, 1辺にあれば2, 2辺にあり、上下or左右を片方ずつ接していれば1 4方を全部囲まれていて、斜め上か斜め下が・の場合・の個数分プラス
ans = 0
for i in range(1, h - 1):

    for j in range(1, w - 1):
        shen = 0
        dhen = 0
        if s[i][j] == '#':
            if s[i - 1][j] != '#':
                shen += 1
            if s[i][j - 1] != '#':
                shen += 1
            if s[i + 1][j] != '#':
                shen += 1
            if s[i][j + 1] != '#':
                shen + 1

            if shen == 4:
                print(4)
                exit()
            if shen == 3:
                ans += 2
            if shen == 2:
                ans += 1
        # ・の場合
        else:
            if s[i - 1][j] == '#':
                dhen += 1
            if s[i][j - 1] == '#':
                dhen += 1
            if s[i + 1][j] == '#':
                dhen += 1
            if s[i][j + 1] == '#':
                dhen + 1

            if dhen == 2:
                ans += 1
            if dhen == 3:
                ans += 2

print(ans)
