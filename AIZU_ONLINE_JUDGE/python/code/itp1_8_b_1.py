while True:
    line = input()
    if line == '0':
        break
    print(sum(map(int, list(line))))