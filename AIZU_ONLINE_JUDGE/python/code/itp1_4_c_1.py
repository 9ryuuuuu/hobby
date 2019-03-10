while True:
    line = input().split()
    a = int(line[0])
    op = str(line[1])
    b = int(line[2])
    if op == '?':
        break
    if op == '+':
        ans = a + b
    if op == '-':
        ans = a - b
    if op == '*':
        ans = a * b
    if op == '/':
        ans = int(a / b)
    print(ans)