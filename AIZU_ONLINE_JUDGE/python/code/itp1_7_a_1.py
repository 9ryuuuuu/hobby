score = []

# 提出用の入力
while True:
    m, f, r = map(int, input().split())
    if m == -1 and f == -1 and r == -1:
        break
    score.append((m, f, r))

# # 動作確認用の入力
# with open('input_itp1_7_a_1.txt', mode='r', encoding='utf8') as input:
#     while True:
#         m, f, r = map(int, next(input).split())
#         if m == -1 and f == -1 and r == -1:
#             break
#         score.append((m, f, r))
# print(score)

for i in range(len(score)):
    sum = score[i][0] + score[i][1]
    if score[i][0] == -1 or score[i][1] == -1 or sum < 30:
        print('F')
    elif sum >= 80:
        print('A')
    elif sum >= 65:
        print('B')
    elif sum >= 50:
        print('C')
    elif sum >= 30:
        if score[i][2] >= 50:
            print('C')
        else:
            print('D')
