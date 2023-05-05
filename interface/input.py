import matplotlib.pyplot as plt


class InputHelper:
    def __init__(self, file_path: str | None = None):
        self.points: list[tuple[float, float]] = []
        if file_path:
            self.read_from_file(file_path=file_path)
        else:
            self.read_from_screen()

    def read_from_screen(self):
        fig, ax = plt.subplots()
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        fig.canvas.mpl_connect("button_press_event", self.onclick)
        plt.title("Choose Points")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    def read_from_file(self, file_path: str) -> list:
        with open(file_path, "r") as file:
            for line in file:
                x, y = map(float, line.strip().split())
                point = (x, y)
                self.points.append(point)

    def onclick(self, event) -> None:
        if event.button == 1:  # Left mouse button click
            self.points.append((round(event.xdata, 2), round(event.ydata, 2)))
            plt.plot(event.xdata, event.ydata, "ro")
            plt.draw()
