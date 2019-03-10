while True:
    card = str(input())
    if card == '-':
        break
    S = int(input())
    for i in range(S):
        h = int(input())
        card = card[h:] + card[:h]
    print(card)