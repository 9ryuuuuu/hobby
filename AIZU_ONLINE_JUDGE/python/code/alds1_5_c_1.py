from math import sin, cos, radians

depth = int(input())


def kock(n: int, p1x: float, p1y: float, p2x: float, p2y: float)-> None:
    if n == 0:
        return

    sx = (2 * p1x + 1 * p2x) / 3
    sy = (2 * p1y + 1 * p2y) / 3
    tx = (1 * p1x + 2 * p2x) / 3
    ty = (1 * p1y + 2 * p2y) / 3
    ux = (tx - sx) * cos(radians(60)) - (ty - sy) * sin(radians(60)) + sx
    uy = (tx - sx) * sin(radians(60)) + (ty - sy) * cos(radians(60)) + sy

    kock(n - 1, p1x, p1y, sx, sy)
    print(f'%10.7f %10.7f' % (sx, sy))
    kock(n - 1, sx, sy, ux, uy)
    print(f'%10.7f %10.7f' % (ux, uy))
    kock(n - 1, ux, uy, tx, ty)
    print(f'%10.7f %10.7f' % (tx, ty))
    kock(n - 1, tx, ty, p2x, p2y)


print(f'%1.7f %1.7f' % (0.0, 0.0))
kock(depth, 0.0, 0.0, 100.0, 0.0)
print(f'%10.7f %10.7f' % (100.0, 0.0))