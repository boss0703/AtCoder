x = input()
m = int(input())
xmax = max([int(c) for c in x])
lx = list(x)
hyoukinum = 0
xmax += 1
for i in range(len(lx)):
    hyoukinum += xmax**(len(lx) - i - 1) * int(lx[i])
if hyoukinum >= m:
    print(0)
    exit()
hyoukinum = 0
cnt = 0
while m >= hyoukinum:
    hyoukinum = 0
    xmax += 1
    for i in range(len(lx)):
        hyoukinum += xmax ** (len(lx) - i - 1) * int(lx[i])
    cnt += 1
print(cnt)
