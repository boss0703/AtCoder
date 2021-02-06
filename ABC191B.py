n, x = map(int, input().split())
a = list(map(int, input().split()))
ans = list()
for i in a:
    if i != x:
        ans.append(i)
if len(ans) != 0:
    print(' '.join(map(str, ans)))
else:
    print('')
