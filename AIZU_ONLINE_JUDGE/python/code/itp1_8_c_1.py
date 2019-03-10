import sys
data = sys.stdin.read()
letters = 'abcdefghijklmnopqrstuvwxyz'
for letter in letters:
    count = 0
    for d in data:
        if letter == d.lower():
            count += 1
    print(f'{letter} : {count}')
