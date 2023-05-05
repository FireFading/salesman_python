import matplotlib.pyplot as plt
from numba import prange


class DrawGraphicsMixin:
    """
    A mixin class for drawing graphics for a given set of points and optimal path.

    """

    def graphics(self) -> None:
        """
        Draw a scatter plot of the points, plots the optimal path,
        and displays the minimum distance of the optimal path.

        """
        plt.figure(figsize=(8, 6))
        x = self.points[:, 0]
        y = self.points[:, 1]

        plt.scatter(x, y, color="blue")
        plt.plot(
            x[[*prange(self.num_points), 0]],
            y[[*prange(self.num_points), 0]],
            color="red",
        )

        optimal_x = [point[0] for point in self.optimal_permutation]
        optimal_y = [point[1] for point in self.optimal_permutation]
        plt.plot(
            optimal_x + [optimal_x[0]],
            optimal_y + [optimal_y[0]],
            linestyle="--",
            color="green",
        )

        for i, (xi, yi) in enumerate(zip(x, y)):
            plt.text(
                xi,
                yi + 0.3,
                str(i + 1),
                color="black",
                fontsize=12,
                ha="center",
                va="center",
            )

        plt.xlabel("X")
        plt.ylabel("Y")

        plt.title(f"Minimum Distance: {self.min_distance}", pad=20)
        plt.legend(["Points", "Optimal Path"])

        plt.subplots_adjust(left=0.15)

        plt.show()
