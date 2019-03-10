import math

# # 動作確認用にファイルから入力
# with open('input_itp1_10_c_1.txt', mode='r') as fin:
#     while True:
#         n = int(next(fin))
#         if n == 0:
#             break
#         data = [int(i) for i in next(fin).split()]
#         mean = sum(data) / n
#         tmp = 0
#         for i in data:
#             tmp += (i - mean)**2
#         print('%f' % (math.sqrt(tmp / n)))

while True:
    n = int(input())
    if n == 0:
        break
    data = [int(i) for i in input().split()]
    mean = sum(data) / n
    tmp = 0
    for i in data:
        tmp += (i - mean)**2
    print('%f' % (math.sqrt(tmp / n)))
