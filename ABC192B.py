s = list(input())
guu = s[0::2]
for m in guu:
    if m.isupper():
        print("No")
        exit()
ki = s[1::2]
for m in ki:
    if m.islower():
        print("No")
        exit()
print("Yes")
