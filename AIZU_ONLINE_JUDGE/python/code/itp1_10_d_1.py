import math

# 提出用
n = int(input())
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]

# # 動作確認用
# with open('input_itp1_10_d_1.txt', mode='r')as fin:
#     n = int(next(fin))
#     x = [int(i) for i in next(fin).split()]
#     y = [int(i) for i in next(fin).split()]

tmp = 0
for i in range(n):
    tmp += abs(x[i] - y[i])
print('%f' % (tmp))

tmp = 0
for i in range(n):
    tmp += (abs(x[i] - y[i]))**2
print('%f' % (math.sqrt(tmp)))

tmp = 0
for i in range(n):
    tmp += (abs(x[i] - y[i]))**3
print('%f' % (pow(tmp, 1 / 3)))

tmp = 0
for i in range(n):
    tmp = abs(x[i] - y[i]) if tmp < abs(x[i] - y[i]) else tmp
print('%f' % (tmp))