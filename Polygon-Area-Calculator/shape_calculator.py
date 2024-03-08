
class Rectangle:
    def __init__(self, width, height):
        self.width= width
        self.height = height
        
    def set_width(self, width):
        self.width = width
    def set_height(self,height):
        self.height = height
    def __str__(self):
        return f"{self.__class__.__name__}(width={self.width}, height={self.height})"
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2* self.width + 2* self.height
    def get_diagonal(self):
        
        return pow(pow(self.width,2) + pow(self.height, 2), 0.5)
        
    def get_picture(self):
        if self.width > 50 or self.height > 50 :
            return ("Too big for picture.")
        else:
            line = "".join(["*" for _ in range(self.width)])+"\n"
            shape =[]
            for i in range(self.height):
                shape.append(line)
            return "".join(shape)
    def get_amount_inside(self, shape):
        return self.get_area()// shape.get_area()
  
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(width = side, height = side)

    def set_side(self, new_side):
        self.side = new_side
        self.width= new_side
        self.height= new_side
    def __str__(self):
        return f"{self.__class__.__name__}(side={self.width})"
