class Intersect:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def orientation(p, q, r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val == 0:
        return 0  # collinear
    elif val > 0:
        return 1  # cw
    else:
        return 2  # ccw


def unless_share_vertices(p1, p2, collide):
    if ((collide.x == p1.x) and (collide.y == p1.y)) or ((collide.x == p2.x) and (collide.y == p2.y)):
        return True


def intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    if o1 != o2 and o3 != o4:
        if unless_share_vertices(p1, q1, p2):
            return False
        if unless_share_vertices(p1, q1, q2):
            return False
        if unless_share_vertices(p2, q2, p1):
            return False
        if unless_share_vertices(p2, q2, q1):
            return False
        return True
    if o1 == 0 and on_seg(p1, p2, q1):
        return True
    if o2 == 0 and on_seg(p1, q2, q1):
        return True
    if o3 == 0 and on_seg(p2, p1, q2):
        return True
    if o4 == 0 and on_seg(p2, q1, q2):
        return True
    return False


def on_seg(p, q, r):
    if q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y):
        return True
    return False


def if_intersect(compare, edge):
    p1 = Intersect(compare[0][0], compare[0][1])
    q1 = Intersect(compare[1][0], compare[1][1])
    p2 = Intersect(edge[0][0], edge[0][1])
    q2 = Intersect(edge[1][0], edge[1][1])
    return intersect(p1, q1, p2, q2)

