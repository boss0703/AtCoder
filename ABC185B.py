# 容量n カフェ回数m 帰宅時刻t
n, m, t = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
l.insert(0, [0, 0])
l.append([t, 0])
ans = 'Yes'
# 現容量o
o = n

for i in range(m + 1):
    # 辿り着ける場合
    if o > (l[i + 1][0] - l[i][1]):
        o = o - (l[i + 1][0] - l[i][1])
        # 充電容量overしない場合
        if n > o + (l[i + 1][1] - l[i + 1][0]):
            o += (l[i + 1][1] - l[i + 1][0])
        else:
            o = n
    else:
        ans = 'No'
        break
print(ans)