# 请编写函数，在已知多边形各条边的长度时，计算多边形的面积。
def tri_area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return s


a, b, c, d, e, f, g = 3, 3, 5, 4, 5, 6, 4
tri_s = (tri_area(a, b, c) + tri_area(c, d, e) + tri_area(e, f, g))
print(tri_s)
