class Point:

    origin = (0, 0)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def tellValue(self):
        print(f"X = {self.x} Y = {self.y}")


p1 = Point(10, 20)
p1.tellValue()
p2 = Point(12, 42)
print(p2.origin, p1.origin, Point.origin)
Point.origin = 90

print(Point.origin)
