order_num = int(input())
jisho = {}
for _i in range(order_num):
    order, key = input().split()
    if order == 'insert':
        jisho[key] = ''
    elif order == 'find':
        try:
            jisho[key]
            print('yes')
        except KeyError:
            print('no')