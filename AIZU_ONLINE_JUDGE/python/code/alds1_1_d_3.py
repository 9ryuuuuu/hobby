"""メモリ資料量をへらすversion

配列にデータを格納しないことで減らす。
"""

N = int(input())

min_v = int(input())
r = int(input())
max_v = r - min_v
if min_v > r:
    min_v = r

for _n in range(2, N):
    r = int(input())
    if max_v < r - min_v:
        max_v = r - min_v
    if min_v > r:
        min_v = r
print(max_v)
