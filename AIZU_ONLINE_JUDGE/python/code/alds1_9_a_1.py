import sys
import math

_n = int(input())
heap = [int(i) for i in input().split()]
heap.insert(0, -sys.maxsize)

for ix, key in enumerate(heap):
    if ix == 0:
        continue

    p_ix = math.floor(ix / 2)
    p_key = heap[p_ix] if p_ix > 0 else sys.maxsize
    l_ix = ix * 2
    l_key = heap[ix * 2] if l_ix < len(heap) else sys.maxsize
    r_ix = ix * 2 + 1
    r_key = heap[ix * 2 + 1] if r_ix < len(heap) else sys.maxsize
    print(f'node {ix}: ', end='')
    print(f'key = {key}, ', end='')
    if p_ix != 0:
        print(f'parent key = {p_key}, ', end='')
    if l_ix < len(heap):
        print(f'left key = {l_key}, ', end='')
    if r_ix < len(heap):
        print(f'right key = {r_key}, ', end='')
    print()
