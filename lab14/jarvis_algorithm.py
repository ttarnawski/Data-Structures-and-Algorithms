from math import inf


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __repr__(self):
        return str(self)


def jarvis_algorythm(points):
    convex_hull = []
    min_x = inf
    for point in points:    # wierzchołek startowy
        if point.x <= min_x:
            if point.x < min_x:
                p = point
                min_x = point.x
            else:
                if point.y < p.y:
                    p = point
                    min_x = point.x
    convex_hull.append(p)

    end_of_hull = False
    while end_of_hull is False:
        for point in points:
            if point not in convex_hull or point == convex_hull[0]:
                q = point
                for r in points:
                    if r != q:
                        if (q.y - p.y) * (r.x - q.x) - (r.y - q.y) * (q.x - p.x) > 0: # prawoskrętne (p, q, r)
                            q = r
                        elif (r.y - p.y) * (q.x - r.x) - (q.y - r.y) * (r.x - p.x) == 0:
                            if q.x == r.x == p.x:
                                if r.y > q.y > p.y or r.y < q.y < p.y:
                                    q = r
                            elif q.y == r.y == p.y:
                                if r.x > q.x > p.x or r.x < q.x < p.x:
                                    q = r
                if q == convex_hull[0]:
                    end_of_hull = True
                    break
                else:
                    convex_hull.append(q)
                    p = q

    return convex_hull

