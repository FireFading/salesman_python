from core.approximate import SalesmanSolver as SalesmanSolverApproximate
from core.brute_force import SalesmanSolver as SalesmanSolverBruteForce
from core.swap import SalesmanSolver as SalesmanSolverSwap
import argparse
from typing import Type, TypeVar

TypeSolver = TypeVar("TypeSolver", SalesmanSolverBruteForce, SalesmanSolverApproximate, SalesmanSolverSwap)

class CommandManager:
    def __init__(self):
        self.classes = {}
        self.file_path, self.algorithm = self.get_command_args()

    @staticmethod
    def get_command_args() -> tuple[str | None, str]:
        parser = argparse.ArgumentParser(description='The salesman problem solver')
        parser.add_argument("--file", "-f", type=str, help="Specify the file name")
        parser.add_argument("--algorithm", "-a", type=str, help="Specify the algorithm to use", choices=["approx", "brute-force", "swap"], default="approx")
        args = parser.parse_args()
        return args.file, args.algorithm

    def register_class(self, name: str, cls: Type[TypeSolver]) -> None:
        self.classes[name] = cls

    def run(self) -> None:
        cls: Type[TypeSolver] = self.classes[self.algorithm]
        instance = cls(file_path=self.file_path)
        instance.solve()
        instance.graphics()


if __name__ == "__main__":
    manager = CommandManager()
    manager.register_class("approx", SalesmanSolverApproximate)
    manager.register_class("brute-force", SalesmanSolverBruteForce)
    manager.register_class("swap", SalesmanSolverSwap)
    manager.run()
