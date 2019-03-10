
# 提出用のインプット
n, m, l = map(int, input().split())
A = [[0] * m for i in range(n)]
B = [[0] * l for i in range(m)]
C = [[0] * l for i in range(n)]
for i in range(n):
    A[i] = [int(i) for i in input().split()]
for i in range(m):
    B[i] = [int(i) for i in input().split()]

# # 動作確認用のインプット
# with open(file='input_itp1_7_d_1.txt', mode='r', encoding='utf8') as input:
#     n, m, l = map(int, next(input).split())
#     A = [[0] * m for i in range(n)]
#     B = [[0] * l for i in range(m)]
#     C = [[0] * l for i in range(n)]
#     for i in range(n):
#         A[i] = [int(i) for i in next(input).split()]
#     print(A)
#     for i in range(m):
#         B[i] = [int(i) for i in next(input).split()]
#     print(B)

for row in range(n):
    for col in range(l):
        tmp = 0
        for k in range(m):
            tmp += A[row][k] * B[k][col]
        C[row][col] = tmp
    print(' '.join(map(str, C[row])))

