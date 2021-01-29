from maze_class import Environment
from os import system


system("clear")
world = Environment()
print(world.maze)
print(world.start_solve())
print(world.maze)