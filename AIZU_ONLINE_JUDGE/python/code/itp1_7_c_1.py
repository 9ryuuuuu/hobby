table = []

# 提出用のインプット
r, c = map(int, input().split())
for i in range(r):
    line = [int(i) for i in input().split()]
    line.append(sum(line))
    table.append(line)

# # 動作確認用のインプット
# with open(file='input_itp1_7_c_1.txt', mode='r', encoding='utf8') as input:
#     r, c = map(int, next(input).split())
#     for i in range(r):
#         line = [int(i) for i in next(input).split()]
#         line.append(sum(line))
#         table.append(line)

for i in range(r):
    print(' '.join(map(str, table[i])))
for j in range(c + 1):
    out = 0
    for i in range(r):
        out += table[i][j]
    if not j == c:
        print(out, end=' ')
    else:
        print(out)