import itertools
from typing import List
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
def largestTriangleArea(self, points: List[List[int]]) -> float:
    def area(a, b, c):
       return 1/2 * abs( # shoelace formula
           a[0] * (b[1] - c[1]) +
           b[0] * (c[1] - a[1]) +
           c[0] + (a[1] - b[1])
       )
    return max(area(*triangle) for triangle in itertools.combinations(points, 3))
    