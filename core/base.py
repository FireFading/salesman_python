import math

import numpy as np
from interface.input import InputHelper
from numba import jit


class SalesmanBase:
    """
    A base class for solving the Traveling Salesman Problem.

    """

    def __init__(self, file_path: str | None = None) -> None:
        """
        Initialize the SalesmanBase instance.

        Args:
        - file_path (str | None): The path to the file containing the TSP data. Defaults to None.

        """
        points = InputHelper(file_path=file_path).points
        self.points = np.array(points)
        self.num_points = len(points)
        self.min_distance = float("inf")
        self.optimal_permutation = None

    @staticmethod
    @jit(nopython=True)
    def distance(point1: tuple[int, int], point2: tuple[int, int]) -> float:
        """
        Calculates the Euclidean distance between two points.

        Args:
        - point1 (tuple[int, int]): The first point as a tuple of (x, y) coordinates.
        - point2 (tuple[int, int]): The second point as a tuple of (x, y) coordinates.

        Returns:
        - The Euclidean distance between the two points.

        """
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

    def update_values(self, distance: float, permutation: list[int]) -> None:
        """
        Update the optimal solution if the given solution is better.

        Args:
        - distance (float): The total distance of the solution.
        - permutation (list[int]): The permutation of the TSP points in the solution.

        """
        if distance < self.min_distance:
            self.min_distance = distance
            self.optimal_permutation = [self.points[i] for i in permutation]

    def solve(self):
        """
        Solves the TSP problem. This method should be implemented in the child class.

        """
        raise NotImplementedError("Specific method not implemented in the child class.")
