class Point:

    def __init__(self, x, y, z):
        self.x = x*x
        self.y = y*y
        self.z = z*z

    def sqSum(self):
        return self.x+self.y+self.z
p = Point(1,3,5)
print(p.sqSum())
