from maze_class import Environment
from os import system


system("clear")
world = Environment()
print(world.maze)
world.start_solve()
world.set_gotos()
print(world.maze)