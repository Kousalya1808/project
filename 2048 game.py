import tkinter as tk
import numpy as np
import random

class Game2048:
    def __init__(self, root):
        self.root = root
        self.root.title("2048 Puzzle")
        self.grid_size = 4
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.score = 0
        self.init_ui()
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def init_ui(self):
        self.frames = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.cells = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 20))
        self.score_label.grid(row=0, column=0, columnspan=self.grid_size)
        
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                frame = tk.Frame(self.root, width=100, height=100, bg="lightgray", borderwidth=1, relief="solid")
                frame.grid(row=i + 1, column=j, padx=5, pady=5)
                self.frames[i][j] = frame
                label = tk.Label(frame, text="", font=("Arial", 24), bg="lightgray")
                label.pack(expand=True, fill="both")
                self.cells[i][j] = label

        self.root.bind("<Up>", lambda _: self.move("up"))
        self.root.bind("<Down>", lambda _: self.move("down"))
        self.root.bind("<Left>", lambda _: self.move("left"))
        self.root.bind("<Right>", lambda _: self.move("right"))
        self.root.bind("r", lambda _: self.restart_game())

    def add_random_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4

    def move(self, direction):
        original_grid = self.grid.copy()
        if direction == "up":
            self.grid = self.move_up(self.grid)
        elif direction == "down":
            self.grid = self.move_up(self.grid[::-1])[::-1]
        elif direction == "left":
            self.grid = self.move_up(self.grid.T).T
        elif direction == "right":
            self.grid = self.move_up(self.grid.T[::-1]).T[::-1]

        if not np.array_equal(original_grid, self.grid):
            self.add_random_tile()
            self.update_ui()
            if self.check_game_over():
                self.show_game_over()

    def move_up(self, grid):
        new_grid = np.zeros_like(grid)
        for col in range(self.grid_size):
            current = [num for num in grid[:, col] if num != 0]
            merged = []
            while current:
                if len(current) > 1 and current[0] == current[1]:
                    merged.append(current[0] * 2)
                    self.score += current[0] * 2
                    current = current[2:]
                else:
                    merged.append(current.pop(0))
            for i, num in enumerate(merged):
                new_grid[i, col] = num
        return new_grid

    def update_ui(self):
        self.score_label.config(text=f"Score: {self.score}")
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.grid[i][j]
                label = self.cells[i][j]
                label.config(text=str(value) if value != 0 else "", bg=self.get_tile_color(value))

    def get_tile_color(self, value):
        colors = {
            0: "lightgray", 2: "lightyellow", 4: "yellow", 8: "orange", 
            16: "red", 32: "darkred", 64: "pink", 128: "lightblue", 
            256: "blue", 512: "purple", 1024: "gold", 2048: "green"
        }
        return colors.get(value, "black")

    def check_game_over(self):
        if 0 in self.grid:
            return False
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if (i + 1 < self.grid_size and self.grid[i, j] == self.grid[i + 1, j]) or \
                   (j + 1 < self.grid_size and self.grid[i, j] == self.grid[i, j + 1]):
                    return False
        return True

    def show_game_over(self):
        self.root.unbind("<Up>")
        self.root.unbind("<Down>")
        self.root.unbind("<Left>")
        self.root.unbind("<Right>")
        game_over_label = tk.Label(self.root, text="Game Over!", font=("Arial", 30), fg="red")
        game_over_label.grid(row=0, column=0, columnspan=self.grid_size)

    def restart_game(self):
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()
        self.init_ui()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game2048(root)
    root.mainloop()
