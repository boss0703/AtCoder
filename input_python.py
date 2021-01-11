# 数値入力 n
n = int(input())
# 一行文字 s[] abc bcd def
s = input().split()
# 一行文字 一文字ずつ s[] a b c d e f
s = list(input().split())
# 一行数値 123 234 3324
nums = list(map(int, input().split()))
# 複数行文字列
# abc
# def
# ghi
s = [input() for _ in range(n)]
# 複数行数値
# 12 23 34
# 42 32 21
# 21 21 43
# 213 321 321
array = [list(map(int, input().split())) for _ in range(n)]
# 単数値 12345 -> 1, 2, 3, 4, 5
s = input()
a = [int(c) for c in s]
# 重複無視　{1, 2, 3, 3, 2} -> {1, 2, 3}
s = set(input() for _ in range(n))

