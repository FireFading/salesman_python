from core.approx import SalesmanSolver as SalesmanSolverApprox
from core.brute_force import SalesmanSolver as SalesmanSolverBruteForce
import argparse
from typing import Type, TypeVar

TypeSolver = TypeVar("TypeSolver", SalesmanSolverBruteForce, SalesmanSolverApprox)

class CommandManager:
    def __init__(self):
        self.classes = {}
        self.file_path, self.algorithm = self.get_command_args()

    @staticmethod
    def get_command_args() -> tuple[str | None, str]:
        parser = argparse.ArgumentParser()
        parser.add_argument("--file", help="Specify the file name")
        parser.add_argument("--algorithm", help="Specify the algorithm to use")
        args = parser.parse_args()
        return args.file, args.algorithm or "approx"

    def register_class(self, name: str, cls: Type[TypeSolver]) -> None:
        self.classes[name] = cls

    def run(self) -> None:
        if self.algorithm not in self.classes:
            raise ValueError("Invalid algorithm name. Try again.")
        cls: Type[TypeSolver] = self.classes[self.algorithm]
        instance = cls(file_path=self.file_path)
        instance.solve()
        instance.graphics()


if __name__ == "__main__":
    manager = CommandManager()
    manager.register_class("approx", SalesmanSolverApprox)
    manager.register_class("brute-force", SalesmanSolverBruteForce)
    manager.run()
