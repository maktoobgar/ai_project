from maze_class import Environment
from os import system


system("clear")
world = Environment()
input()
print(world.maze)
input()
world.start_solve()
input()
world.set_gotos()
print(world.maze)