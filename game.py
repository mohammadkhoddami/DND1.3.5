from map import Map
from player import Player
from enemy import Dragon
from door import Door
from Login import Login
from player import Key
import os
import time
# import logging.config

# dont use star to import classes. only import the class itself DONE

#logging configuration
# logging.config.fileConfig("config.toml", disable_existing_loggers=False)
# logger = logging.getLogger(__name__)
# gameLog = logging.getLogger("gameLogger")
# userLog = logging.getLogger("userLogger")


gameboard = Map()
player = Player()
dragon = Dragon()
dungeon = Door()
login = Login()
key = Key()

# all of this block should be implemented in a while loop. DONE
# add confirm password to your register method to be able to check DONE
# both passwords entered are the same. DONE


while True:
    loginreg = input("login or register?(l , r) : ")
    if loginreg == "r":
        user = input("chose your username : ")
        password = input("chose your password : ")
        confrim_password = input("repeat your password : ")
        if password == confrim_password:
            pass
        else:
            print("passwords doesn`t match")
        login.register(user, password)
    if loginreg == "l":
        user = input("what is you username : ")
        password = input("what is your password : ")
        if login.login(user, password):
            break

gamerun = True
while gamerun:
    grid = gameboard.create_map()
    # grid_whole = gameboard.dungeon_whole_area()
    # dungeon_whole_x, dungeon_whole_y =gameboard.create_dungeon_whole(grid)
    dragon_x, dragon_y = dragon.create_dragon(grid)
    door_x, door_y = dungeon.create_door(grid)
    key.create_key(grid)
    player_x, player_y = player.startpoint(grid, dragon_x)
    dragon_x, dragon_y = dragon.dragonmovment(grid, player_x, player_y)
    having_key = key.key_usage(grid, player_x, player_y)
    dropping_in_whole = gameboard.dropped_in_whole(grid, player_x, player_y)
    # player_x, player_y = player.startpoint(grid, dragon_x)
    gameboard.draw_map()
    player.endgame(grid, dragon_x, dragon_y, door_x, door_y, having_key )
    player_move = input("move (w,a,s,d): ")
    # player.endgame(grid, dragon_x, dragon_y, door_x, door_y, having_key , dungeon_whole_x , dungeon_whole_y)
    # player_move = input("move (w,a,s,d): ")
    player_x, player_y = player.movement(grid, player_move)
    os.system("cls")
    print(player_x, player_y)
    print(dragon_x, dragon_y)
    print(door_x, door_y)
    print(having_key)
    # print(dungeon_whole_x, dungeon_whole_y)
    print(dropping_in_whole)


# check flake8 in every file DONE
# add clear screen to the project DONE


# usernames must be encrypted and passwords should be hash
# use hashlib for this 
# SHA 256 , SHA 512
