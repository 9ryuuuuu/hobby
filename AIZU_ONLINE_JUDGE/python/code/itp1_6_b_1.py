N = int(input())
cards = []
for i in range(N):
    line = input().split()
    cards.append((line[0], int(line[1])))

tarinai_list = []
for a in ['S', 'H', 'C', 'D']:
    for num in range(1, 14):
        find = False
        for card in cards:
            if a == card[0] and num == card[1]:
                find = True
                break
        if not find:
            tarinai_list.append((a, num))
for l in tarinai_list:
    print(' '.join(map(str, l)))