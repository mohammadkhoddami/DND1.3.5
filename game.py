from map import Map
from player import Player
from enemy import Dragon
from door import Door
from Login import Login
from player import Key
import os


"""
this is the main file of our game.

"""
gameboard = Map()
player = Player()
dragon = Dragon()
dungeon = Door()
login = Login()
key = Key()


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
    dragon_x, dragon_y = dragon.create_dragon(grid)
    door_x, door_y = dungeon.create_door(grid)
    key.create_key(grid)
    player_x, player_y = player.startpoint(grid, dragon_x)
    dragon_x, dragon_y = dragon.dragonmovment(grid, player_x, player_y)
    having_key = key.key_usage(grid, player_x, player_y)
    gameboard.draw_map()
    player_move = input("move (w,a,s,d): ")
    player_x, player_y = player.movement(grid, player_move)
    player.endgame(grid, dragon_x, dragon_y, door_x, door_y, having_key )
    os.system("cls")


    """
    for debuging use below printts
    
    """

    # print(dragon_x, dragon_y)
    # print(door_x, door_y)
    # print(having_key)
    # print(dropping_in_whole)