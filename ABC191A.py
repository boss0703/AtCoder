v, t, s, d = map(int, input().split())
time = d / v

if t <= time <= s:
    print('No')
else:
    print('Yes')
