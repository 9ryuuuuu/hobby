"""x,y の最大公約数を求める。

以下の性質を用いる。
x >= y のとき、x, y の最大公約数は、y と x % y の最大公約数に等しい。
"""

x, y = map(int, input().split())

if x < y:
    x, y = y, x
while y > 0:
    x, y = y, x % y
print(x)
