A = []
b = []

# 提出用の入力処理
n, m = map(int, input().split())
for i in range(n):
    A.append([int(i) for i in input().split()])
for i in range(m):
    b.append(int(input()))

# # テスト用にファイルから入力する処理
# with open('input_itp1_6_d_1.txt', mode='r', encoding='utf8') as f:
#     n, m = map(int, next(f).split())
#     try:
#         for i in range(n):
#                 A.append([int(i) for i in next(f).split()])
#         for i in range(m):
#             b.append(int(next(f)))
#     except StopIteration:
#         raise ValueError('入力データがおかしい')

for row in range(len(A)):
    tmp = 0
    for col in range(len(A[row])):
        tmp += A[row][col] * b[col]
    print(tmp)