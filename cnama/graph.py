from abc import ABC, abstractmethod
from typing import List

class IGraph(ABC):
    @property
    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def __getitem__(self, index: tuple) -> int:
        pass

    @abstractmethod
    def __setitem__(self, index: tuple, cost: int):
        pass

    @abstractmethod
    def add_edge(self, a: int, b: int, cost: int):
        pass

    @abstractmethod
    def get_neighbours(self, a: int) -> List[int]:
        pass

class AdjacencyMatrix(IGraph):
    NO_EDGE = -1

    def __init__(self, n: int):
        if n < 0:
            raise ValueError("Invalid node count")
        self._count = n
        self.data = [[self.NO_EDGE for _ in range(n)] for _ in range(n)]

    @property
    def count(self) -> int:
        return self._count

    def __getitem__(self, index: tuple) -> int:
        a, b = index
        return self.data[a][b]

    def __setitem__(self, index: tuple, cost: int):
        a, b = index
        self.add_edge(a, b, cost)

    def add_edge(self, a: int, b: int, cost: int):
        if cost < 0:
            raise ValueError("Invalid edge cost")
        self.data[a][b] = cost

    def get_neighbours(self, a: int) -> List[int]:
        neighbours = []
        for i in range(self._count):
            if self.data[a][i] != self.NO_EDGE:
                neighbours.append(i)
        return neighbours

    def __str__(self) -> str:
        rows = len(self.data)
        cols = len(self.data[0])
        max_width = self._find_max_value_width(self.data)

        sb = []
        # Header row with column numbers
        sb.append(" " * (max_width + 1))
        for i in range(cols):
            sb.append(f"{str(i).rjust(max_width)} ")
        sb.append("\n")

        # Separator row
        sb.append(" " * (max_width + 1))
        for i in range(cols):
            sb.append("-" * max_width + "-")
        sb.append("\n")

        # Data rows
        for i in range(rows):
            sb.append(f"{i}| ")
            for j in range(cols):
                if self.data[i][j] != self.NO_EDGE:
                    sb.append(f"{str(self.data[i][j]).rjust(max_width)} ")
                else:
                    sb.append(f"{'-'.rjust(max_width)} ")
            sb.append("\n")

        return ''.join(sb)

    def _find_max_value_width(self, data) -> int:
        max_width = 0
        for row in data:
            for value in row:
                value_length = len(str(value))
                if value_length > max_width:
                    max_width = value_length
        return max_width
