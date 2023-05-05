from core.aprox import SalesmanSolver
from utils import get_command_args


if __name__ == "__main__":
    file_path = get_command_args()
    solve = SalesmanSolver(file_path=file_path)
    solve.solve()
    solve.graphics()