import itertools
from collections.abc import Iterator

from core.base import SalesmanBase
from interface.output import DrawGraphicsMixin
from numba import prange
from utils import measure_execution_time


class SalesmanSolver(SalesmanBase, DrawGraphicsMixin):
    """
    A solver class that implements the SalesmanBase and DrawGraphicsMixin classes
    to solve the Traveling Salesman Problem.

    Uses brute-force approach to find the shortest path.

    """

    def __init__(self, file_path: str | None = None) -> None:
        """
        Initialize a new instance of the class.

        Args:
        - file_path (str | None): The path to the file containing the coordinates of the points.

        """
        super().__init__(file_path=file_path)
        self.permutations = self.get_permutation()

    def get_permutation(self) -> Iterator[int]:
        """
        Return an iterator that generates all possible permutations of the indices of the points.

        Returns:
        - permutations (Iterator[int]): An iterator that generates all possible
        permutations of the indices of the points.

        """
        indices = tuple(prange(self.num_points))
        return itertools.permutations(indices)

    def calculate_distance(self, permutation: tuple[int]) -> float:
        """
        Calculate the total distance of a permutation of the points.

        Args:
        - permutation (tuple[int]): A permutation of the indices of the points.

        Returns:
        - total_distance (float): The total distance of the permutation.

        """
        total_distance = 0
        for point in prange(self.num_points - 1):
            current_point = permutation[point]
            next_point = permutation[point + 1]
            total_distance += self.distance(point1=self.points[current_point], point2=self.points[next_point])
        total_distance += self.distance(point1=self.points[permutation[-1]], point2=self.points[permutation[0]])
        return total_distance

    @measure_execution_time
    def solve(self) -> None:
        """
        Find the optimal permutation of the points that gives the shortest total distance.

        """
        for permutation in self.permutations:
            distance = self.calculate_distance(permutation=permutation)
            self.update_values(distance=distance, permutation=permutation)
