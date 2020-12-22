num = input()
nums = list(map(int, input().split()))
cnt = 0
while 1 not in [i % 2 for i in nums]:
    cnt += 1
    nums = [d / 2 for d in nums]
print(cnt)