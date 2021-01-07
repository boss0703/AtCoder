n = int(input())
s = set(input() for _ in range(n))
ans = "satisfiable"
for word in s:
    if "!" + word in s:
        ans = word
        break
print(ans)
