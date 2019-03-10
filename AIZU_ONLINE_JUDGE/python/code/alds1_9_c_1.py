from heapq import heappush, heappop


p_que = []
while True:
    line = input().split()
    if line[0] == 'end':
        break
    elif line[0] == 'insert':
        val = int(line[1])
        heappush(p_que, -val)
    elif line[0] == 'extract':
        print(-1 * heappop(p_que))
    else:
        raise ValueError('想定外の事態')
