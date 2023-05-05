import itertools

from core.base import SalesmanBase
from interface.output import DrawGraphicsMixin
from utils import measure_execution_time


class SalesmanSolver(SalesmanBase, DrawGraphicsMixin):
    def __init__(self, file_path: str | None = None):
        super().__init__(file_path=file_path)
        self.initial_permutations = self.generate_initial_permutations()

    def calculate_distance(self, permutation: list[str]) -> float:
        total_distance = 0
        for point in range(self.num_points - 1):
            current_point = permutation[point]
            next_point = permutation[point + 1]
            total_distance += self.distance(point1=self.points[current_point], point2=self.points[next_point])
        total_distance += self.distance(point1=self.points[permutation[-1]], point2=self.points[permutation[0]])
        return total_distance

    def generate_initial_permutations(self) -> list[int]:
        indices = tuple(range(self.num_points))
        return list(itertools.islice(itertools.permutations(indices), self.num_points))

    def perform_swap(self, permutation: list[int], i: int, j: int) -> list[int]:
        new_permutation = permutation[:]
        new_permutation[i], new_permutation[j] = new_permutation[j], new_permutation[i]
        return new_permutation

    @measure_execution_time
    def solve(self, num_swaps: int = 2) -> None:
        for initial_permutation in self.initial_permutations:
            current_permutation = initial_permutation[:]
            current_distance = self.calculate_distance(permutation=current_permutation)

            for _ in range(num_swaps):
                for i in range(-1, self.num_points):
                    for j in range(i + 1, self.num_points):
                        new_permutation = self.perform_swap(permutation=list(current_permutation), i=i, j=j)
                        new_distance = self.calculate_distance(permutation=new_permutation)
                        if new_distance < current_distance:
                            current_permutation = new_permutation
                            current_distance = new_distance

            self.update_values(distance=current_distance, permutation=current_permutation)
