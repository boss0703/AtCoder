n = int(input())
array = list(map(int, input().split()))
a = b = 0
for i in range(0, n):
    if i % 2 == 0:
        a += max(array)
    else:
        b += max(array)
    array[array.index(max(array))] = 0
print(a-b)
