class Point:
    def __init__(self, xy) -> None:
        self.x = xy[0]
        self.y = xy[1]
    def __repr__(self) -> str:
        return "(" + str(self.x) + "," + str(self.y) + ")"

def most_left(points):
    p = Point((float('inf'),float('inf')))
    for el in points:
        if el.x < p.x:
            p = el
        elif el.x == p.x:
            if el.y < p.y:
                p = el
    return p

def orientation(p,q,r):
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if val > 0:     #prawoskrętne
        return 1
    elif val == 0:  #współliniowe
        return 0
    else:           #lewoskrętne
        return -1

def jarvis(points):
    p = most_left(points)
    temp = p
    result = []
    while temp:
        result.append(p)
        q = points[(points.index(p)+1) % len(points)]
        for r in (points):
            if orientation(p, r, q) == -1:
                q = r
        p = q
        if p == temp:
            break

    return result

def jarvis_v2(points):
    p = most_left(points)
    temp = p
    result = []
    while temp:
        result.append(p)
        q = points[(points.index(p)+1) % len(points)]
        for r in points:
            if orientation(p, r, q) == -1:
                q = r
            elif orientation(p, r, q) == 0:
                if p.x < q.x < r.x:
                    q = r
                elif r.x < q.x < p.x:
                    q = r
                elif p.x == r.x == q.x and p.y < q.y < r.y:
                    q = r
                elif p.x == r.x == q.x and r.y < q.y < p.y:
                    q = r
        p = q
        if p == temp:
            break

    return result



def main():
    p_1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    points_1 = []
    for i in p_1:
        points_1.append(Point(i))
    
    print(jarvis(points_1))

    p_2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    points_2 = []
    for i in p_2:
        points_2.append(Point(i))
    
    print(jarvis(points_2))
    print(jarvis_v2(points_2))

    p_3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    points_3 = []
    for i in p_3:
        points_3.append(Point(i))
    
    print(jarvis(points_3))
    print(jarvis_v2(points_3))

main()