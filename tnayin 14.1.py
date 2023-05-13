class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Area(self):
        print("area is ", 2*(self.length + self.width), "sm^2")
    def Perimeter(self):
        print("perimeter is ", self.length * self.width, "sm")

orientation = input("enter word` area or perimeter\n")
lenght = int(input("input length:\t"))
width = int(input("input width:\t"))
area = Rectangle(lenght, width)
perimeter = Rectangle(lenght, width)
if orientation == "area":
    area.Area()
elif orientation == perimeter:
    perimeter.Perimeter()
else:
    print("kayword is NotFound")