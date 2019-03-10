from queue import Queue

n, q_time = map(int, input().split())
qu = Queue()
for i in range(n):
    p_name, p_time = input().split()
    p_time = int(p_time)
    qu.put((p_name, p_time))

t = 0
while True:
    if qu.empty():
        break
    p_name, p_time = qu.get()
    if p_time <= q_time:
        t += p_time
        print(f'{p_name} {t}')
    else:
        t += q_time
        qu.put((p_name, p_time - q_time))
