n, x = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
x *= 100

for i in range(n):
    x -= array[i][0] * array[i][1]
    if x < 0:
        print(i + 1)
        exit()

print(-1)

