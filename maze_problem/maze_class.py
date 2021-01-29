from random import randrange
from enum import Enum


class Colors:
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


class State(Enum):
    """Describes how we finished the algorithm"""
    Failure = 0
    Victory = 1


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
        self.f = None
        self.g = None
        self.blocked_directions = []
        self.parent = None
        self.goto = None
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
        """Calls sizecheck function of neighbor node on his direction side"""
        if direction == Direction.right and not direction in self.blocked_directions:
            if self.y + 1 > 9:
                return False
            if not maze.nodes[self.x, self.y + 1].sizecheck():
                return False
        elif direction == Direction.left and not direction in self.blocked_directions:
            if self.y - 1 < 0:
                return False
            if self.y - 1 < 0 and not maze.nodes[self.x, self.y - 1].sizecheck():
                return False
        elif direction == Direction.down and not direction in self.blocked_directions:
            if self.x + 1 > 9:
                return False
            if self.x + 1 > 9 and not maze.nodes[self.x + 1, self.y].sizecheck():
                return False
        elif direction == Direction.up and not direction in self.blocked_directions:
            if self.x - 1 < 0:
                return False
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
    
    def f_set(self, g):
        """Returns hueristic value of the node"""
        self.g = g
        self.f = g + self.h()
        return self.f
    
    def h(self):
        """Returns estimated cost to the goal"""
        return abs(self.x - goal.x) + abs(self.y - goal.y)

    def is_this_allowed(self, direction):
        """Determines if moving to the given direction in allowed or not"""
        if direction in self.blocked_directions:
            return False
        return True
    
    def __str__(self):
        if self.parent:
            return "x: " + str(self.x) + ", y: " + str(self.y) + " - blocked = " + str(self.blocked_directions) + " - parent = x: " + str(self.parent.x) + ", y: " + str(self.parent.y)
        else:
            return "x: " + str(self.x) + ", y: " + str(self.y) + " - blocked = " + str(self.blocked_directions)


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
        """Draw the maze"""
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
                        if Direction.right == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{red}|{green}G{end}{end}{green}>{end}'
                        else:
                            rl[i] = rl[i] + f'{red}|{green}G{end}{end} '
                    elif me.x == i and me.y == j:
                        if Direction.right == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{red}|{green}*{end}{end}{green}>{end}'
                        else:
                            rl[i] = rl[i] + f'{red}|{green}*{end}{end} '
                    else:
                        if Direction.right == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{red}|{green} {end}{end}{green}>{end}'
                        else:
                            rl[i] = rl[i] + f'{red}|{end}  '
                elif Direction.right in self.nodes[i, j].blocked_directions:
                    if goal.x == i and goal.y == j:
                        if Direction.left == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{green}<{end}{green}G{end}{red}|{end}'
                        else:
                            rl[i] = rl[i] + f' {green}G{end}{red}|{end}'
                    elif me.x == i and me.y == j:
                        if Direction.left == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{green}<{end}{green}*{end}{red}|{end}'
                        else:
                            rl[i] = rl[i] + f' {green}*{end}{red}|{end}'
                    else:
                        if Direction.left == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{green}<{end}{green} {end}{red}|{end}'
                        else:
                            rl[i] = rl[i] + f'  {red}|{end}'
                else:
                    if goal.x == i and goal.y == j:
                        if Direction.left == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{green}<{end}{green}G{end} '
                        elif Direction.right == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f' {green}G{end}{green}>{end}'
                        else:
                            rl[i] = rl[i] + f' {green}G{end} '
                    elif me.x == i and me.y == j:
                        if Direction.left == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{green}<{end}{green}*{end} '
                        elif Direction.right == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f' {green}*{end}{green}>{end}'
                        else:
                            rl[i] = rl[i] + f' {green}*{end} '
                    else:
                        if Direction.left == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f'{green}<{end}{green} {end} '
                        elif Direction.right == self.nodes[i, j].goto:
                            rl[i] = rl[i] + f' {green} {end}{green}>{end}'
                        else:
                            rl[i] = rl[i] + f' {green} {end} '
        down = [''] * 10
        for i in range(10):
            for j in range(10):
                if Direction.down in self.nodes[i, j].blocked_directions:
                    if j == 0:
                        down[i] = down[i] + f'{red}|--{end}'
                    elif j == 9:
                        down[i] = down[i] + f'{red}--|{end}'
                    else:
                        down[i] = down[i] + f'{red}---{end}'
                elif Direction.down == self.nodes[i, j].goto:
                    if j == 0:
                        down[i] = down[i] + f'{red}|{end}{green}v{end} '
                    elif j == 9:
                        down[i] = down[i] + f' {green}v{end}{red}|{end}'
                    else:
                        down[i] = down[i] + f' {green}v{end} '
                elif Direction.up == self.nodes[i + 1, j].goto:
                    if j == 0:
                        down[i] = down[i] + f'|{green}^{end} '
                    elif j == 9:
                        down[i] = down[i] + f' {green}^{end}|'
                    else:
                        down[i] = down[i] + f' {green}^{end} '
                else:
                    if j == 0:
                        down[i] = down[i] + f'{red}|  {end}'
                    elif j == 9:
                        down[i] = down[i] + f'{red}  |{end}'
                    else:
                        down[i] = down[i] + f'   '
        output = f'{red}|--{end}' + f'{red}---{end}'*8 + f'{red}--|{end}' + '\n'
        for i in range(10):
            output = output + rl[i] + '\n' + down[i] + '\n'
        return output


class Environment:
    """My Main usable, direct access class in main that everything is in it"""

    def __init__(self):
        maze.blocks()
        self.maze = maze
        self.me = me
        self.goal = goal
        self.fringe = []
        self.closed = []

    def start_solve(self):
        """Initialization for A* Algorithm"""
        self.fringe = []
        self.closed = []
        node = maze.nodes[me.x, me.y]
        node.f_set(0)
        self.fringe.append(node)
        situation = self.solve()
        if situation == State.Victory:
            self.set_gotos()
        return situation
    
    def solve(self):
        """Actually solve the algorithm"""
        while(True):
            if not self.fringe:
                return State.Failure
            node = self.lowest_node()
            if node.x == goal.x and node.y == goal.y:
                return State.Victory
            if node.is_this_allowed(Direction.up):
                temp_node = maze.nodes[node.x - 1, node.y]
                if temp_node in self.closed:
                    tempf = temp_node.f
                    if tempf > temp_node.f_set(node.g + 1):
                        temp_node.parent = node
                        self.closed.remove(temp_node)
                        self.fringe.append(temp_node)
                elif temp_node in self.fringe:
                    tempf = temp_node.f
                    tempg = temp_node.g
                    if tempf < temp_node.f_set(node.g + 1):
                        temp_node.f = tempf
                        temp_node.g = tempg
                    elif tempf > temp_node.f:
                        temp_node.parent = node
                else:
                    temp_node.f_set(node.g + 1)
                    temp_node.parent = node
                    self.fringe.append(temp_node)
            if node.is_this_allowed(Direction.down):
                temp_node = maze.nodes[node.x + 1, node.y]
                if temp_node in self.closed:
                    tempf = temp_node.f
                    if tempf > temp_node.f_set(node.g + 1):
                        temp_node.parent = node
                        self.closed.remove(temp_node)
                        self.fringe.append(temp_node)
                elif temp_node in self.fringe:
                    tempf = temp_node.f
                    tempg = temp_node.g
                    if tempf < temp_node.f_set(node.g + 1):
                        temp_node.f = tempf
                        temp_node.g = tempg
                    elif tempf > temp_node.f:
                        temp_node.parent = node
                else:
                    temp_node.f_set(node.g + 1)
                    temp_node.parent = node
                    self.fringe.append(temp_node)
            if node.is_this_allowed(Direction.right):
                temp_node = maze.nodes[node.x, node.y + 1]
                if temp_node in self.closed:
                    tempf = temp_node.f
                    if tempf > temp_node.f_set(node.g + 1):
                        temp_node.parent = node
                        self.closed.remove(temp_node)
                        self.fringe.append(temp_node)
                elif temp_node in self.fringe:
                    tempf = temp_node.f
                    tempg = temp_node.g
                    if tempf < temp_node.f_set(node.g + 1):
                        temp_node.f = tempf
                        temp_node.g = tempg
                    elif tempf > temp_node.f:
                        temp_node.parent = node
                else:
                    temp_node.f_set(node.g + 1)
                    temp_node.parent = node
                    self.fringe.append(temp_node)
            if node.is_this_allowed(Direction.left):
                temp_node = maze.nodes[node.x, node.y - 1]
                if temp_node in self.closed:
                    tempf = temp_node.f
                    if tempf > temp_node.f_set(node.g + 1):
                        temp_node.parent = node
                        self.closed.remove(temp_node)
                        self.fringe.append(temp_node)
                elif temp_node in self.fringe:
                    tempf = temp_node.f
                    tempg = temp_node.g
                    if tempf < temp_node.f_set(node.g + 1):
                        temp_node.f = tempf
                        temp_node.g = tempg
                    elif tempf > temp_node.f:
                        temp_node.parent = node
                else:
                    temp_node.f_set(node.g + 1)
                    temp_node.parent = node
                    self.fringe.append(temp_node)
    
    def set_gotos(self):
        """Determine movement direction on nodes in path to the goal"""
        node = maze.nodes[goal.x, goal.y]
        parent = node.parent
        while parent:
            if parent.x - 1 == node.x:
                parent.goto = Direction.up
            elif parent.x + 1 == node.x:
                parent.goto = Direction.down
            elif parent.y - 1 == node.y:
                parent.goto = Direction.left
            elif parent.y + 1 == node.y:
                parent.goto = Direction.right
            node = parent
            parent = parent.parent
    
    def lowest_node(self):
        """Get the lowest cost node in the fringe"""
        lowest = self.fringe[0]
        lowest_index = 0
        for i in range(len(self.fringe)):
            if lowest.f > self.fringe[i].f:
                lowest = self.fringe[i]
                lowest_index = i
        self.closed.append(lowest)
        self.fringe.pop(lowest_index)
        return lowest

    def __str__(self):
        return self.maze.__str__()


red = f'{Colors.FAIL}{Colors.BOLD}'
green = f'{Colors.OKGREEN}{Colors.BOLD}'
yellow = f'{Colors.BOLD}{Colors.WARNING}'
end = f'{Colors.ENDC}{Colors.ENDC}'
get_dir = [Direction.right, Direction.left, Direction.up, Direction.down]
me = Position(0, 0)
goal = Position(9, 9)
maze = Maze()