"""不正解の回答。

このやり方では「連続した荷物」という条件を満たせない。
"""


buggage_num, track_num = map(int, input().split())
weights = [int(input()) for i in range(buggage_num)]

track_weights = [0 for i in range(track_num)]
j = 0
for weight in reversed(sorted(weights)):
    # 荷物の積まれたトラックの中から、最も積載量が少ないトラックを取得する処理
    min_weight = track_weights[0]
    min_index = 0
    for i, track_weight in enumerate(track_weights):
        if track_weight < min_weight:
            min_weight = track_weight
            min_index = i

    track_weights[min_index] += weight
    print(f'{weight} -> {min_index}')
print(' '.join(map(str, track_weights)))
print(max(track_weights))