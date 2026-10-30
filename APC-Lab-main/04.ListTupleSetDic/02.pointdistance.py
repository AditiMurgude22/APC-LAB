import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 +
                     (p2[1] - p1[1]) ** 2)

def farthest_from_origin(points):
    farthest = points[0]
    max_distance = distance((0, 0), farthest)

    for point in points:
        d = distance((0, 0), point)

        if d > max_distance:
            max_distance = d
            farthest = point

    return farthest


points = [(2, 3), (5, 1), (-4, 6), (1, 2)]

print("Points:", points)

p1 = points[0]
p2 = points[1]

print("Distance between", p1, "and", p2, "=", distance(p1, p2))

print("Farthest point from origin:",
      farthest_from_origin(points))
