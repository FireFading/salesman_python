import numpy as np
from core.base import SalesmanBase
from interface.output import DrawGraphicsMixin
from numba import prange
from utils import measure_execution_time


class SalesmanSolver(SalesmanBase, DrawGraphicsMixin):
    """
    A solver class that implements the SalesmanBase and DrawGraphicsMixin classes
    to solve the Traveling Salesman Problem.

    Uses a greedy algorithm to find the shortest path.

    """

    def __init__(self, file_path: str | None = None) -> None:
        """
        Initialize the SalesmanSolver instance.

        Args:
        - file_path (str | None): The path to the file containing the TSP data. Defaults to None.

        """
        super().__init__(file_path=file_path)
        self.distance_matrix = np.zeros((self.num_points, self.num_points))

        self.calc_distance_matrix()

    def calc_distance_matrix(self) -> None:
        """
        Calculate the distance matrix for the given TSP data.

        """
        for i in prange(self.num_points):
            for j in prange(self.num_points):
                point1, point2 = self.points[i], self.points[j]
                self.distance_matrix[i][j] = self.distance(point1=point1, point2=point2)

    def search(self, start: int = 0) -> tuple[list[int], float]:
        """
        Search for the optimal TSP solution from the starting point using the nearest neighbor algorithm.

        Args:
        - start (int): The starting point index. Defaults to 0.

        Returns:
        - A tuple containing the optimal permutation of points and the total distance of the route.

        """
        current, permutation, distance = start, [start], 0
        visited = {start}

        while len(visited) < self.num_points:
            distance_vector = self.distance_matrix[current]
            min_index = min(
                (num_point for num_point, _ in enumerate(distance_vector) if num_point not in visited),
                key=distance_vector.__getitem__,
            )

            permutation.append(min_index)
            visited.add(min_index)
            distance += distance_vector[min_index]
            current = min_index

        distance += self.distance_matrix[min_index][start]
        return permutation, distance

    @measure_execution_time
    def solve(self) -> None:
        """
        Solve the TSP problem by calling the search function for all the starting points.

        """
        for i in prange(self.num_points):
            permutation, distance = self.search(i)
            self.update_values(distance=distance, permutation=permutation)
