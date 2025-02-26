class Circle:
    def __init__(self, radius):
        self.radius = radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        print(f"Drawing a rectangle with width {self.width} and height {self.height}")
        return self.height * self.width

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        if shape_type == "Circle":
            return Circle(*args)
        elif shape_type == "rectangle":
            return Rectangle(*args)
        else:
            raise ValueError("Unknown shape type")

shape1 = ShapeFactory.create_shape("Circle", 5)

shape2 = ShapeFactory.create_shape("rectangle", 10, 30)

shape1.draw()
se = shape2.draw()
print(se)