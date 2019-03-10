N = int(input())
taro_cnt, hana_cnt = 0, 0
for _i in range(N):
    taro, hana = map(str, input().split())
    if taro > hana:
        taro_cnt += 3
    elif taro == hana:
        taro_cnt += 1
        hana_cnt += 1
    else:
        hana_cnt += 3
print(f'{taro_cnt} {hana_cnt}')