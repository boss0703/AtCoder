n, k = map(int, input().split())
ln = []
for i in range(k):
    ln = list(str(n))
    sot = int(''.join(sorted(ln)))
    rev = int(''.join(sorted(ln, reverse=True)))
    n = rev - sot
print(n)
