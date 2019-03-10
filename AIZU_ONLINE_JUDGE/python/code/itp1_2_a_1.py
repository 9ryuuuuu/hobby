data = [int(i) for i in input().split()]
if data[0] < data[1]:
    print('a < b')
elif data[0] > data[1]:
    print('a > b')
else:
    print('a == b')
