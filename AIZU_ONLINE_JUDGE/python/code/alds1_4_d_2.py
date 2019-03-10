import math
from typing import List

buggage_num, truck_num = map(int, input().split())
buggage_list = [int(input()) for i in range(buggage_num)]


def able_to_load_buggage(max_weight: int,
                         truck_num: int, buggage_list: List[int]) -> bool:
    i = 0
    truck = [0 for i in range(truck_num + 1)]
    for buggage in buggage_list:
        if truck[i] + buggage <= max_weight:
            truck[i] += buggage
        else:
            i += 1
            truck[i] += buggage
        if i > (truck_num - 1):
            return False
    for t in truck:
        if t > max_weight:
            return False
    else:
        return True


# data = [i for i in range(31)]
# for d in data:
#     result = able_to_load_buggage(d, truck_num, buggage_list)
#     print(f'{d} {result}')

left = 0
right = 100000 * 10000 + 1
i = 0
while left < right:
    i += 1
    mid = math.floor((left + right) / 2)
    result = able_to_load_buggage(mid, truck_num, buggage_list)
    # print(f'{i} {left} {mid} {right} {result}')
    if result:
        right = mid
    else:
        left = mid + 1
# print(f'{left} {mid} {right}')
print(left)
