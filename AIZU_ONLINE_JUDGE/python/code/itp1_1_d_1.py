total_sec = int(input())
h = int(total_sec / 3600)
last_seconds = total_sec % 3600
m = int(last_seconds / 60)
s = last_seconds % 60
print(f'{h}:{m}:{s}')
