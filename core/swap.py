import itertools

from core.base import SalesmanBase
from interface.output import DrawGraphicsMixin
from numba import prange
from utils import measure_execution_time


class SalesmanSolver(SalesmanBase, DrawGraphicsMixin):
    """
    A solver class that implements the SalesmanBase and DrawGraphicsMixin classes
    to solve the Traveling Salesman Problem.

    Uses a swap algorithm to find the shortest path.

    """

    def __init__(self, file_path: str | None = None):
        """
        Initialize the SalesmanSolver object.

        Args:
        - file_path: A string representing the path to the input file. Default is None.

        """
        super().__init__(file_path=file_path)
        self.initial_permutations = self.generate_initial_permutations()

    def calculate_distance(self, permutation: list[str]) -> float:
        """
        Calculate the total distance of a given permutation of points.

        Args:
        - permutation: A list of integers representing the order of the points.

        Returns:
        - A float representing the total distance of the given permutation of points.

        """
        total_distance = 0
        for point in prange(self.num_points - 1):
            current_point = permutation[point]
            next_point = permutation[point + 1]
            total_distance += self.distance(point1=self.points[current_point], point2=self.points[next_point])
        total_distance += self.distance(point1=self.points[permutation[-1]], point2=self.points[permutation[0]])
        return total_distance

    def generate_initial_permutations(self) -> list[int]:
        """
        Generate a list of initial permutations of the points.

        Returns:
        - A list of tuples representing the initial permutations of the points.

        """
        indices = tuple(prange(self.num_points))
        return list(itertools.islice(itertools.permutations(indices), self.num_points))

    def perform_swap(self, permutation: list[int], i: int, j: int) -> list[int]:
        """
        Perform a swap operation on the given permutation.

        Args:
        - permutation: A list of integers representing the current order of the points.
        - i: An integer representing the index of the first point to swap.
        - j: An integer representing the index of the second point to swap.

        Returns:
        - A new list representing the permutation after the swap operation is performed.

        """
        new_permutation = permutation[:]
        new_permutation[i], new_permutation[j] = new_permutation[j], new_permutation[i]
        return new_permutation

    @measure_execution_time
    def solve(self, num_swaps: int = 2) -> None:
        """
        Solve the traveling salesman problem using a local search approach.

        Args:
        - num_swaps: An integer representing the number of swaps to perform. Default is 2.

        """
        for initial_permutation in self.initial_permutations:
            current_permutation = initial_permutation[:]
            current_distance = self.calculate_distance(permutation=current_permutation)

            for _ in prange(num_swaps):
                for i in prange(-1, self.num_points):
                    for j in prange(i + 1, self.num_points):
                        new_permutation = self.perform_swap(permutation=list(current_permutation), i=i, j=j)
                        new_distance = self.calculate_distance(permutation=new_permutation)
                        if new_distance < current_distance:
                            current_permutation = new_permutation
                            current_distance = new_distance

            self.update_values(distance=current_distance, permutation=current_permutation)
