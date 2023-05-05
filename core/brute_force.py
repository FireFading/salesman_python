import itertools
from collections.abc import Iterator

from core.base import SalesmanBase
from interface.output import DrawGraphicsMixin
from utils import measure_execution_time


class SalesmanSolver(SalesmanBase, DrawGraphicsMixin):
    def __init__(self, file_path: str | None = None) -> None:
        super().__init__(file_path=file_path)
        self.permutations = self.get_permutation()

    def get_permutation(self) -> Iterator[int]:
        indices = tuple(range(self.num_points))
        return itertools.permutations(indices)

    def calculate_distance(self, permutation: tuple[int]) -> float:
        total_distance = 0
        for point in range(self.num_points - 1):
            current_point = permutation[point]
            next_point = permutation[point + 1]
            total_distance += self.distance(point1=self.points[current_point], point2=self.points[next_point])
        total_distance += self.distance(point1=self.points[permutation[-1]], point2=self.points[permutation[0]])
        return total_distance

    @measure_execution_time
    def solve(self) -> None:
        for permutation in self.permutations:
            distance = self.calculate_distance(permutation=permutation)
            self.update_values(distance=distance, permutation=permutation)
