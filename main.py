import math
from square_generator import SquareGenerator
# 1
# squares = [x**2 for x in range(1, 11)]
# print(squares)

# 2
# def e_squares(start, end):
#     squares = [x**2 for x in range(start, end + 1)]
#     return squares
#
#
# print(e_squares(5, 12))

# 3
# class SquareGenerator:
#     def generate_squares(self, start, end):
#         squares = []
#         for num in range(start, end + 1):
#             squares.append(num ** 2)
#         return squares
#
#
# start_num = 2
# end_num = 15
#
# square_gen = SquareGenerator()
#
# squares_list = square_gen.generate_squares(start_num, end_num)
# print("From", start_num, "to", end_num, ":", squares_list)
#
#
# 4
# square_roots = [math.sqrt(num) for num in squares_list]
# print("Squares Roots:", square_roots)

# 5
# class SquareGenerator:
#     def generate_squares(self, start, end):
#         if start > end:
#             raise Exception("start is greater than end")
#
#         squares = []
#         for num in range(start, end + 1):
#             squares.append(num ** 2)
#         return squares
#
#
# start_num = 2
# end_num = 1
#
# square_gen = SquareGenerator()
#
# squares_list = square_gen.generate_squares(start_num, end_num)
# print("From", start_num, "to", end_num, ":", squares_list)


# 6
start_num = 1
end_num = 7

square_gen = SquareGenerator()

squares_list = square_gen.generate_squares(start_num, end_num)
print("From", start_num, "to", end_num, ":", squares_list)
