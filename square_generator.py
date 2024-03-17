# 6
class SquareGenerator:
    def generate_squares(self, start, end):
        if start > end:
            raise Exception("start is greater than end")

        squares = []
        for num in range(start, end + 1):
            squares.append(num ** 2)
        return squares


