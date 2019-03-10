S = str(input())
N = int(input())
for _i in range(N):
    line = input().split()
    start = int(line[1])
    end = int(line[2])

    if line[0] == 'print':
        print(S[start:end + 1])
    if line[0] == 'reverse':
        reversed_word = list(S[start:end + 1])
        reversed_word.reverse()
        S = S[:start] + ''.join(reversed_word) + S[end + 1:]
    if line[0] == 'replace':
        S = S[:start] + line[3] + S[end + 1:]
