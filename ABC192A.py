x = input()
if int(x) > 100:
    sita = int(x[-2]) * 10 + int(x[-1])
else:
    sita = int(x)
print(100-sita)