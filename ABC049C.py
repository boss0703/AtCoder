s = input()
words = ["dream", "dreamer", "erase", "eraser"]
while True:
    ans = "NO"
    for word in words:
        # 前から詰めていく方法だと語尾のer, rで困ったので後ろから詰める
        if s.endswith(word):
            s = s[:-len(word)]
            ans = "YES"
            break
    # リストが空の場合
    if not s:
        break
    if ans == "NO":
        break
print(ans)