from map import Map
import random


class Flash(Map):
    def __init__(self) -> None:
        self.up_point_x = random.randint(2, 7)
        self.up_point_y = random.randint(2, 7)

    def placement(self, grid):
        grid[self.up_point_x][self.up_point_y] = "🟥"
        return self.up_point_x, self.up_point_y

    def get_speed(self, grid, player_x, player_y, dragon_x, dragon_y):
        if grid[player_x][player_y] == grid[self.up_point_x][self.up_point_y]:
            grid[dragon_x][dragon_y] = "🐉"
