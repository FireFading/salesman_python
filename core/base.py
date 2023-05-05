import math

import numpy as np
from interface.input import InputHelper


class SalesmanBase:
    def __init__(self, file_path: str | None = None) -> None:
        points = InputHelper(file_path=file_path).points
        self.points = np.array(points)
        self.num_points = len(points)
        self.min_distance = float("inf")
        self.optimal_permutation = None

    @staticmethod
    def distance(point1: tuple[int, int], point2: tuple[int, int]) -> float:
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def solve(self):
        raise NotImplementedError("Specific method not implemented in the child class.")
