from queen_class import Environment
from os import system


system("clear")
world = Environment()
print(world.board)
world.start_solve()
print(world.board)