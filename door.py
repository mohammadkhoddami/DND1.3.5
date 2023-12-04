import random


class Door:
    def __init__(self) -> None:
        self.door_x = random.randint(0, 9)
        self.door_y = random.randint(0, 9)

    def create_door(self, grid):
        grid[self.door_x][self.door_y] = "🟩"
        return self.door_x, self.door_y


"""
note : 
write a funtion for the time that door and dragon being in same position.
should be used after dragon , player , dungeon and before draw map 
it`s need a file at least!
"""
