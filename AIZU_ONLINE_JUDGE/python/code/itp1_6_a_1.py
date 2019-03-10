n = int(input())
a = [int(i) for i in input().split()]
out = ' '.join([str(i) for i in list(reversed(a))])
print(out)
