import random
"""
the map is created by x and y (like math) and it`s nested list


"""

#create map
class Map:
    def __init__(self) -> None:
        self.x = 10
        self.y = 10
        self.grid = []
        self.row = []
        self.square = "🟩"
        self.whole_suqare = "🟥"
        self.dungeon_whole_x = random.randint(0, 9)
        self.dungeon_whole_y = random.randint(0, 9)
        self.whole_x = 20
        self.whole_y = 20
        self.grid_whole = []
        self.row_whole = []
        self.dropping_in_whole = False
    def create_map(self):
        self.grid = [] 
        for i in range(self.x):
            self.row = []  
            self.grid.append(self.row)
            for i in range(self.y):
                self.row.append(self.square)
        return self.grid
#drawing map
    def draw_map(self):
        for i in (self.grid):
            print(' '.join(i))

# it`s a feature but isn`t active yet
    # def create_dungeon_whole(self, grid):
    #     grid[self.dungeon_whole_x][self.dungeon_whole_y] = "🟩"
    #     return self.dungeon_whole_x, self.dungeon_whole_y
        
    # def dungeon_whole_area(self):
    #     self.grid_whole = []
    #     for i in range (self.whole_x):
    #         self.row_whole = []
    #         self.grid_whole.append(self.row_whole)
    #         for i in range (self.whole_y):
    #             self.row_whole.append(self.whole_suqare)
    #     return self.grid_whole
    
    # def draw_whole(self):
    #     for i in (self.grid_whole):
    #         print(" ".join(i))
    
    # def dropped_in_whole(self, grid, player_x, player_y):
    #     if grid[player_x][player_y] == grid[self.dungeon_whole_x][self.dungeon_whole_y]:
    #         self.dropping_in_whole = True
    #         print("you dropped on dungeon whole")
    #     return self.dropping_in_whole