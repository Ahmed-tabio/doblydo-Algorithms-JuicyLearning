# points belongs to 2-D, The Closest is the minimum Euclidean distance
import math

p = [(1, 2), (2, 9), (3, 4), (12, 9), (3, 8)]

def euclidean_dis(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# O(n^2)
def brute_force(points2d):
    assert len(points2d) > 1
    p1 = points2d[0]
    p2 = points2d[1]
    minimumd = euclidean_dis(p1, p2)
    if len(points2d) == 2:
        return p1, p2, minimumd
    for i in range(len(points2d)-1):
        for j in range(i+1, len(points2d)):
            p1 = points2d[i]
            p2 = points2d[j]
            d = euclidean_dis(p1, p2)
            if minimumd < d:
                minimumd = d
    return p1, p2, minimumd
# ============================================================
# Divide and Conquer: can we beat Quadratic Time?
def closest_split_pair(px, py, delta):
    mideanx = px[len(px)//2][0]
    Sy = [sy for sy in py if (mideanx - delta) <= sy[0] <= (mideanx + delta)]
    best = delta
    for i in range(len(Sy)-1): # O(n): worst case
        for j in range(i+1, min(i+7, len(Sy))): # O(1)
            if euclidean_dis(Sy[i], Sy[j]) < best:
                p1, p2, best = Sy[i], Sy[j], euclidean_dis(Sy[i], Sy[j])
    return p1, p2, best


def closest_pair(px, py):
    if len(px) <= 3:
        return brute_force(px)

    Lx = px [:len(px)//2]
    Rx = px [len(px)//2:]

    midx = px[len(px)//2][0]
    Ly = [ly for ly in py if ly[0] <= midx]
    Ry = [ry for ry in py if ry[0] >  midx]

    l1, l2, dist1  = closest_pair(Lx, Ly)
    r1, r2, dist2  = closest_pair(Rx, Ry)
    p1, p2, delta  = (l1, l2, dist1) if dist1 < dist2 else (r1, r2, dist2)
    sp1, sp2, dist = closest_split_pair(px, py, delta)
    if dist < delta:
        return sp1, sp2, dist
    else:
        return p1, p2, delta

def call_closest_pair_on(points):
    px = sorted(points, key=lambda x: x[0])
    py = sorted(points, key=lambda x: x[1])
    return closest_pair(px, py)

print(call_closest_pair_on(p))

# ==
