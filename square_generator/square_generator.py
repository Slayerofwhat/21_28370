# 6, 7
class SquareGenerator:
    def generate_squares(self, start, end):
        if start > end:
            raise Exception("start is greater than end")

        squares = []
        for num in range(start, end + 1):
            squares.append(num ** 2)
        return squares


# 8
class CubeGenerator(SquareGenerator):
    def generate_cubes(self, start, end):
        if start > end:
            raise Exception("start is greater than end")

        cubes = []
        for num in range(start, end + 1):
            cubes.append(num ** 3)
        return cubes

# 9

    def generate_squares(self, start, end):
        if start > end:
            raise Exception("start is greater than end")

        squares = []
        for num in range(start, end + 1):
            squares.append(num ** 2)
        return squares
