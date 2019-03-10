from collections import deque

n = int(input())
d = deque()
for _i in range(n):
    line = input().split()
    order = line[0]
    if order in ('insert', 'delete'):
        key = line[1]
    if order == 'insert':
        d.appendleft(key)
    elif order == 'delete':
        try:
            d.remove(key)
        except ValueError:
            pass
    elif order == 'deleteFirst':
        d.popleft()
    elif order == 'deleteLast':
        d.pop()
    else:
        raise ValueError('Invalid order: {order}')

print(' '.join(d))
