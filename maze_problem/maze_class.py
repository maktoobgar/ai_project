from random import randrange
from enum import Enum


class bcolors:
    """Just a color class for showing results in colors"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Direction(Enum):
    """An enum for our moving directions for better code readability"""
    right = 0
    left = 1
    up = 2
    down = 3


class Position:
    """Our Start and Goal positions are made of 'Position Class'"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "x: " + str(x) + ", y: " + str(y)


class Node:
    """Every point in our 2D array is made of a 'Node Class'"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.blocked_directions = []
        self.block_around()
    
    def block_around(self):
        """If the node is on the edge, blocks edges"""
        if self.y + 1 > 9:
            self.blocked_directions.append(Direction.right)
        if self.y - 1 < 0:
            self.blocked_directions.append(Direction.left)
        if self.x + 1 > 9:
            self.blocked_directions.append(Direction.down)
        if self.x - 1 < 0:
            self.blocked_directions.append(Direction.up)

    def block_it(self, direction):
        """Blocks movement to a direction"""
        if not self.sizecheck() or not self.has_permission(direction):
            return False
        self.perform_block(direction)
        return True
        
    def has_permission(self, direction):
        """Calls sizecheck function of neighbor node"""
        if direction == Direction.right and not direction in self.blocked_directions:
            if not maze.nodes[self.x, self.y + 1].sizecheck():
                return False
        elif direction == Direction.left and not direction in self.blocked_directions:
            if self.y - 1 < 0 and not maze.nodes[self.x, self.y - 1].sizecheck():
                return False
        elif direction == Direction.down and not direction in self.blocked_directions:
            if self.x + 1 > 9 and not maze.nodes[self.x + 1, self.y].sizecheck():
                return False
        elif direction == Direction.up and not direction in self.blocked_directions:
            if self.x - 1 < 0 and not maze.nodes[self.x - 1, self.y].sizecheck():
                return False
        return True

    def perform_block(self, direction):
        """Blocks the direction in the node and it's neighbor node"""
        if direction == Direction.right and not direction in self.blocked_directions:
            self.blocked_directions.append(Direction.right)
            maze.nodes[self.x, self.y + 1].blocked_directions.append(Direction.left)
        elif direction == Direction.left and not direction in self.blocked_directions:
            self.blocked_directions.append(Direction.left)
            maze.nodes[self.x, self.y - 1].blocked_directions.append(Direction.right)
        elif direction == Direction.down and not direction in self.blocked_directions:
            self.blocked_directions.append(Direction.down)
            maze.nodes[self.x + 1, self.y].blocked_directions.append(Direction.up)
        elif direction == Direction.up and not direction in self.blocked_directions:
            self.blocked_directions.append(Direction.up)
            maze.nodes[self.x - 1, self.y].blocked_directions.append(Direction.down)

    def sizecheck(self):
        """Every node have a limit for blocking It's own neighbors, That limit will be checked here"""
        if len(self.blocked_directions) >= 3:
            return False
        return True
    
    def opposite(self, dir):
        """Returns opposite direction of dir"""
        if dir == Direction.left:
            return Direction.right
        elif dir == Direction.right:
            return Direction.left
        elif dir == Direction.up:
            return Direction.down
        elif dir == Direction.down:
            return Direction.up
    
    def __str__(self):
        return "x: " + str(self.x) + ", y: " + str(self.y) + "\nblocked = " + str(self.blocked_directions)


class Maze:
    """The maze of the problem, generates random blocks and random field"""

    def __init__(self):
        self.nodes = {}
        for i in range(10):
            for j in range(10):
                self.nodes[i, j] = Node(i, j)
    
    def blocks(self):
        """Making random blocks for maze"""
        # maximum possible number of blocks in a 10x10 nodes is 90
        blocknum = randrange(60, 90)
        print(f'{yellow}generating {blocknum} blocks...{end}')
        for num in range(blocknum):
            blocked = False
            while(not blocked):
                x = randrange(10)
                y = randrange(10)
                randrlud = randrange(4)
                direction = get_dir[randrlud]
                blocked = self.nodes[x, y].block_it(direction)
        print(f'{green}generating the world is done.{end}')

    def __str__(self):
        top = [''] * 10
        for i in range(10):
            for j in range(10):
                if Direction.up in self.nodes[i, j].blocked_directions:
                    top[i] = top[i] + f' {red}-{end} '
                else:
                    top[i] = top[i] + '   '
        rl = [''] * 10
        for i in range(10):
            for j in range(10):
                if Direction.left in self.nodes[i, j].blocked_directions and Direction.right in self.nodes[i, j].blocked_directions:
                    if goal.x == i and goal.y == j:
                        rl[i] = rl[i] + f'{red}|{green}G{end}{red}|{end}'
                    elif me.x == i and me.y == j:
                        rl[i] = rl[i] + f'{red}|{green}*{end}{red}|{end}'
                    else:
                        rl[i] = rl[i] + f'{red}| |{end}'
                elif Direction.left in self.nodes[i, j].blocked_directions:
                    if goal.x == i and goal.y == j:
                        rl[i] = rl[i] + f'{red}|{green}G{end}{end} '
                    elif me.x == i and me.y == j:
                        rl[i] = rl[i] + f'{red}|{green}*{end}{end} '
                    else:
                        rl[i] = rl[i] + f'{red}|{end}  '
                elif Direction.right in self.nodes[i, j].blocked_directions:
                    if goal.x == i and goal.y == j:
                        rl[i] = rl[i] + f' {green}G{end}{red}|{end}'
                    elif me.x == i and me.y == j:
                        rl[i] = rl[i] + f' {green}*{end}{red}|{end}'
                    else:
                        rl[i] = rl[i] + f'  {red}|{end}'
                else:
                    if goal.x == i and goal.y == j:
                        rl[i] = rl[i] + f' {green}G{end} '
                    elif goal.x == i and goal.y == j:
                        rl[i] = rl[i] + f' {green}*{end} '
                    else:
                        rl[i] = rl[i] + f'   '
        down = [''] * 10
        for i in range(10):
            for j in range(10):
                if Direction.down in self.nodes[i, j].blocked_directions:
                    down[i] = down[i] + f' {red}-{end} '
                else:
                    down[i] = down[i] + f'   '
        output = ''
        for i in range(10):
            output = output + top[i] + '\n' + rl[i] + '\n' + down[i] + '\n'
        return output


class Environment:
    """My Main usable, direct access class in main that everything is in it"""

    def __init__(self):
        maze.blocks()
        self.me = me
        self.goal = goal
        self.maze = maze

    def __str__(self):
        return self.maze


red = f'{bcolors.FAIL}{bcolors.BOLD}'
green = f'{bcolors.OKGREEN}{bcolors.BOLD}'
yellow = f'{bcolors.BOLD}{bcolors.WARNING}'
end = f'{bcolors.ENDC}{bcolors.ENDC}'
get_dir = [Direction.right, Direction.left, Direction.up, Direction.down]
me = Position(0, 0)
goal = Position(9, 9)
maze = Maze()
