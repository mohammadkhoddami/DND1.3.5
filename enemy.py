import random

"""
This file is for enemies that i craeted if player x y and enemy x y equals --> player will lose the game


"""

# dragon class
class Dragon:
    def __init__(self) -> None:
        self.dragon_x = random.randint(0, 9)
        self.dragon_y = random.randint(0, 9)
        self.d = 0
# create dragon
    def create_dragon(self, grid):
        grid[self.dragon_x][self.dragon_y] = "🟩"
        return self.dragon_x, self.dragon_y
# dragon movement logic
    def dragonmovment(self, grid, player_x, player_y):
        self.d = ((player_x - self.dragon_x) ** 2 + (player_y - self.dragon_y) ** 2) ** 0.5
        self.chance = random.randint(0, 9)
        if self.d == 3 and self.chance <= 2:
            if player_x > self.dragon_x:
                self.dragon_x += 1
            elif player_x < self.dragon_x:
                self.dragon_x -= 1
            elif player_y > self.dragon_y:
                self.dragon_y += 1
            elif player_y < self.dragon_y:
                self.dragon_y -= 1
        if self.d <= 2:
            grid[self.dragon_x][self.dragon_y] = "🐉"
            if self.chance <= 3:
                if player_x > self.dragon_x:
                    self.dragon_x += 1
                elif player_x < self.dragon_x:
                    self.dragon_x -= 1
                elif player_y > self.dragon_y:
                    self.dragon_y += 1
                elif player_y < self.dragon_y:
                    self.dragon_y -= 1
            print("The Dragon is near, run!")
        if self.d == 1 and self.chance <= 8:
            if player_x > self.dragon_x:
                self.dragon_x += 1
            elif player_x < self.dragon_x:
                self.dragon_x -= 1
            elif player_y > self.dragon_y:
                self.dragon_y += 1
            elif player_y < self.dragon_y:
                self.dragon_y -= 1
        return self.dragon_x, self.dragon_y
