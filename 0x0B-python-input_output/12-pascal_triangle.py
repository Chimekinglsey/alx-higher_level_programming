#!/usr/bin/python3
""" MODULE 13: PASCAL'S TRIANGLE"""


def pascal_triangle(n):
    """
       This function returns a list of lists of ints rep\
       representing Pascal's triangle of n
    """
    my_list = []
    if n <= 0:
        return my_list
    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
    return my_list
