a, b = input().split()
ans = sum(list(map(int, a)))
if ans < sum(list(map(int, b))):
    ans = sum(list(map(int, b)))
print(ans)
