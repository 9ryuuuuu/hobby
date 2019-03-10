n = int(input())
a = [int(i) for i in input().split()]
a.reverse()
print(' '.join(map(str, a)))
