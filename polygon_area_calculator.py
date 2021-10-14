class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        str = f'Rectangle(width={self.width}, height={self.height})'
        return str

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return (self.width)*(self.height)

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return (self.width**2 + self.height**2 )**0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        else:
            # pic = ''
            # for j in range(self.height):
            #     pic += self.width*'*' + '\n'
            pic = (self.width*'*' + '\n')*self.height
            return pic

    def get_amount_inside(self, tile):
        if tile.width > self.width or tile.height > self.height:
            return 0
        else:
            fits_per_row = self.width // tile.width
            fits = fits_per_row * (self.height // tile.height)
        return fits

class Square(Rectangle):
    def __init__(self, side):
        self.width = self.height = side

    def __str__(self):
        str = f'Square(side={self.width})'
        return str

    def set_width(self, new_side):
        self.width = self.height = new_side

    def set_height(self, new_side):
        self.width = self.height = new_side

    def set_side(self, new_side):
        self.width = self.height = new_side



# tests
rect = Rectangle(2,2)
print(rect.get_picture() )
tile = Rectangle(1,1)
print(rect.get_amount_inside(tile) )

square = Square(2)
square.set_width(1)
print(square.get_picture() )
print(square)


# alternative
# pic += self.width*'*' + (j//(self.height - 1) + 1)%2 *'\n'
