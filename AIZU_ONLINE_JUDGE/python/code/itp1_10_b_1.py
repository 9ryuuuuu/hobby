import math
a, b, C = map(int, input().split())
print('%f' % (0.5 * a * b * math.sin(math.radians(C))))
c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(math.radians(C)))
print('%f' % (a + b + c))
print('%f' % (b * math.sin(math.radians(C))))
