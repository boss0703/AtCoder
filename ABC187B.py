def calc_slope(x1, y1, x2, y2):
    return (y1 - y2) / (x1 - x2)


n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    if n == 1:
        break
    for j in range(i+1, n):
        slope = calc_slope(array[i][0], array[i][1], array[j][0], array[j][1])
        if (slope >= -1.0) & (slope <= 1.0):
            ans += 1
print(ans)