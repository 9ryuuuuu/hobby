N = int(input())
S = [int(i) for i in input().split()]
q = int(input())
T = [int(i) for i in input().split()]


count = 0
for t in T:
    S.append(t)
    i = 0
    while t != S[i]:
        i += 1
    if i != (len(S) - 1):
        count += 1
    S.pop()
print(count)
