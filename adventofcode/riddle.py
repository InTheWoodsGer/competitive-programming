class MatrixRiddle:

    def __init__(self, riddle: str, starting_index: int = 0):
        self._matrix = [line for line in riddle.splitlines()]
        self._x_length = len(self._matrix[0])
        self._y_length = len(self._matrix)
        self._starting_index = starting_index

    def __str__(self):
        print("\n".join(self._matrix))

