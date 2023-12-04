import random


"""
This is the dungeon door if player x y going equal to dungeon door x y --> player will win the game and gonna escape from the dungeon
"""


class Door:
    def __init__(self) -> None:
        self.door_x = random.randint(0, 9)
        self.door_y = random.randint(0, 9)

    def create_door(self, grid):
        grid[self.door_x][self.door_y] = "🟩"
        return self.door_x, self.door_y


