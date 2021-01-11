n = int(input())
cnt = 2 ** n
a = list(map(int, input().split()))
length = len(a)
array2 = []

for l in range(n):
    if l == 0:
        array = list(range(0, length))
    for i in range(0, length - 1, 2):
        if a[array[i]] > a[array[i+1]]:
            array2.append(array[i])
            if length == 2:
                print(array[1] + 1)
        else:
            array2.append(array[i+1])
            if length == 2:
                print(array[0] + 1)
    array = array2
    array2 = []
    length = len(array)







