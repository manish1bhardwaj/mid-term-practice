class Rectangle:
    def area(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def perimeter(self,length,breadth):
        self.length = length
        self.breadth = breadth
#main code
#area
Area  = Rectangle()
Area.Length = 20
Area.Breadth = 2
area_of_rect = Area.Length*Area.Breadth
print(area_of_rect)

#perimeter
Perimeter = Rectangle()
Perimeter.Length = 30
Perimeter.Breadth = 40
perimeter_of_rect = 2*(Perimeter.Length+Perimeter.Breadth)
print(perimeter_of_rect)