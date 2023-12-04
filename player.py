from map import Map
import sys
import random


class Player(Map):
    def __init__(self) -> None:
        # super().__init__()
        self.player_x = random.randint(0, 9)
        self.player_y = random.randint(0, 9)
        self.dropped_in_whole = False
    def startpoint(self, grid, dragon_x):
        grid[self.player_x][self.player_y] = "🤺"
        try:
            self.player_x != dragon_x
        except:
            self.player_x = random.randint(0, 9)
        return self.player_x, self.player_y

    def movement(self, grid, move):
        if move == "a" and self.player_y != 0:
            grid[self.player_y][self.player_x] = "🟩"
            self.player_y -= 1
            grid[self.player_y][self.player_x] = "🤺"
        elif move == "d" and self.player_y != 9:
            grid[self.player_y][self.player_x] = "🟩"
            self.player_y += 1
            grid[self.player_y][self.player_x] = "🤺"
        elif move == "s" and self.player_x != 9:
            grid[self.player_y][self.player_x] = "🟩"
            self.player_x += 1
            grid[self.player_y][self.player_x] = "🤺"
        elif move == "w" and self.player_x != 0:
            grid[self.player_y][self.player_x] = "🟩"
            self.player_x -= 1
            grid[self.player_y][self.player_x] = "🤺"
        else:
            print("invalid input")
        return self.player_x, self.player_y

    def endgame(self, grid, dragon_x, dragon_y, door_x, door_y, having_key):
        if grid[self.player_x][self.player_y] == grid[dragon_x][dragon_y] and self.player_x == dragon_x and self.player_y == dragon_y:
            sys.exit("Sorry Dragon Eats you")
        elif grid[self.player_x][self.player_y] == grid[door_x][door_y] and self.player_x == door_x and self.player_y == door_y:
            if having_key == True:
                sys.exit("Yaaaay! you escape from dungeon")
            else:
                print("you are on the door but u don`t have key")


class Key:
    def __init__(self) -> None:
        self.key_x = random.randint(0, 9)
        self.key_y = random.randint(0, 9)
        self.having_key = False

    def create_key(self, grid):
        grid[self.key_x][self.key_y] = "🟩"
        return self.key_x, self.key_y

    def key_usage(self, grid, player_x, player_y):
        if grid[player_x][player_y] == grid[self.key_x][self.key_y]:
            self.having_key = True
            print("you find key, now you can run!")
        print(self.key_x, self.key_y)
        return self.having_key
