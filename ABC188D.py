n, c = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    array[1][i] - array[0][i]