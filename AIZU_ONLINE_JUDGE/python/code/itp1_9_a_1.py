W = str(input())
words = []
while True:
    line = str(input())
    if line == 'END_OF_TEXT':
        break
    words += line.lower().split()

cnt = 0
for word in words:
    if W == word:
        cnt += 1
print(cnt)
