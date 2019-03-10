from collections import deque

n = int(input())
d = deque()
for _i in range(n):
    order = input()
    if order == 'deleteFirst':
        d.popleft()
    elif order == 'deleteLast':
        d.pop()
    else:
        order, key = order.split()
        if order == 'insert':
            d.appendleft(key)
        elif order == 'delete':
            try:
                d.remove(key)
            except ValueError:
                pass
        else:
            raise ValueError('Invalid order: {order}')

print(' '.join(d))
