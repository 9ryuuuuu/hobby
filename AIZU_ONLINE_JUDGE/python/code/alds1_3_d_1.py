# 参考URL
# https://mtdtx9.hatenablog.com/entry/2017/04/24/230941

lines = input()
stack_1 = []

area = 0
for i, line in enumerate(lines):
    if line == '\\':
        stack_1.append(i)
    elif line == '_':
        pass
    elif line == '/':
        if not stack_1 == []:
            this_area = i - stack_1.pop()
            area += this_area
    else:
        raise ValueError('Unexpected line: {i}, {line}')
print(area)
if area > 0:
    print(f'1 {area}')
else:
    print(f'0')
