from rectangle import Rectangle, Square, Round

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print(rect_1.get_area())
print(rect_2.get_area())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

round_1 = Round(13)
round_2 = Round(7)

print(round_1.get_area_round(),
      round_2.get_area_round())

figures = [rect_1, rect_2, square_1, square_2, round_1, round_2]
for figure in figures:
    if isinstance(figure, Square):
        print(figure.get_area_square())
    elif isinstance(figure, Round):
        print(figure.get_area_round())
    else:
        print(figure.get_area())


