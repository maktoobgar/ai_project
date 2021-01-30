from random import randrange
from datetime import datetime
from enum import Enum
from os import system
import time


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


class Direction(Enum):
    """An enum for our moving directions for better code readability"""
    right = 0
    left = 1
    up = 2
    down = 3


class Node:
    """Node Class"""
    def __init__(self, x, y, queen):
        self.x = x
        self.y = y
        self.f = None
        self.queen = False
        self.set_queen(queen)

    def set_queen(self, queen):
        if queen:
            if self.queen:
                return True
            else:
                self.queen = True
                queens.append(self)
                return True
        else:
            if self.queen:
                queens.remove(self)
                self.queen = False
                return False
            else:
                return False

    def set_f(self):
        f = 0
        for i in range(0, self.x):
            if board.nodes[i, self.y].queen:
                f = f + 1
        for i in range(self.x + 1, 8):
            if board.nodes[i, self.y].queen:
                f = f + 1
        for j in range(0, self.y):
            if board.nodes[self.x, j].queen:
                f = f + 1
        for j in range(self.y + 1, 8):
            if board.nodes[self.x, j].queen:
                f = f + 1
        i = self.x - 1
        j = self.y - 1
        while i > 0 and j > 0:
            if board.nodes[i, j].queen:
                f = f + 1
            i = i - 1
            j = j - 1
        i = self.x - 1
        j = self.y + 1
        while i > 0 and j < 8:
            if board.nodes[i, j].queen:
                f = f + 1
            i = i - 1
            j = j + 1
        i = self.x + 1
        j = self.y - 1
        while i < 8 and j > 0:
            if board.nodes[i, j].queen:
                f = f + 1
            i = i + 1
            j = j - 1
        i = self.x + 1
        j = self.y + 1
        while i < 8 and j < 8:
            if board.nodes[i, j].queen:
                f = f + 1
            i = i + 1
            j = j + 1
        self.f = f
        return f


class Board:

    def __init__(self):
        self.nodes = {}
        for i in range(0, 8):
            for j in range(0, 8):
                self.nodes[i, j] = Node(i, j, False)
        for i in range(0, 8):
            j = randrange(8)
            self.nodes[i, j].set_queen(True)
        
    def __str__(self):
        rl = [''] * 8
        for i in range(8):
            for j in range(8):
                if self.nodes[i, j].queen and j == 0:
                    rl[i] = rl[i] + f'{red}|{end}{green}Q{end}|'
                elif self.nodes[i, j].queen and j == 7:
                    rl[i] = rl[i] + f'{green}Q{end}{red}|{end}'
                elif j == 0:
                    rl[i] = rl[i] + f'{red}|{end} |'
                elif j == 7:
                    rl[i] = rl[i] + f' {red}|{end}'
                elif self.nodes[i, j].queen:
                    rl[i] = rl[i] + f'{green}Q{end}|'
                else:
                    rl[i] = rl[i] + f' |'
        output = f'{red}|--{end}' + f'{red}--{end}'*6 + f'{red}-|{end}' + '\n'
        for i in range(8):
            if i >= 7:
                output = output + rl[i] + '\n' + f'{red}|--{end}' + f'{red}--{end}'*6 + f'{red}-|{end}' + '\n'
                break
            output = output + rl[i] + '\n' + f'{red}|{end}- ' + '- '*6 + f'-{red}|{end}' + '\n'
        return output


class Environment:

    def __init__(self):
        self.board = board
        self.elapsed_time = 0

    def __str__(self):
        return self.board.__str__()
    
    def start_solve(self):
        start_time = datetime.now()
        for i in range(0, 100000):
            if self.cost() == 0:
                break
            num = randrange(len(queens))
            queen = queens[num]
            if queen.set_f() == 0:
                continue
            self.simulated_anealing(queen, [10, 8, 6, 4, 2, 0])
        end_time = datetime.now()
        self.elapsed_time = (end_time - start_time).microseconds / 1000
        print("Success, Elapsed Time: %sms" % (str(self.elapsed_time)))

    def simulated_anealing(self, current, schedule):
        direction = None
        rand = True
        for t in range(len(schedule)):
            self.update_f()
            T = schedule[t]
            if T == 0:
                return
            next = self.next(current, direction, rand)
            if not next:
                return
            dE = next.f - current.f
            rand = False
            if dE > 0:
                current.set_queen(False)
                next.set_queen(True)
                current = next
                direction = self.direction(current, next)
                #system("clear")
                #print(self.board)
                #time.sleep(0.01)
                continue
            else:
                rand = randrange(10)
                if rand < (e ** (dE / T)) * 10:
                    current.set_queen(False)
                    next.set_queen(True)
                    current = next
                    direction = self.direction(current, next)
                    #system("clear")
                    #print(self.board)
                    #time.sleep(0.01)
                    continue
            break

    def update_f(self):
        for queen in queens:
            queen.set_f()

    def direction(self, current, next):
        if current.y + 1 < 8:
            if current.y < next.y:
                return Direction.right
        if current.y - 1 > -1:
            if current.y > next.y:
                return Direction.left
    
    def next(self, current, direction, rand):
        if direction:
            if direction == Direction.left:
                if current.y - 1 < 0:
                    return None
                return self.board.nodes[current.x, current.y - 1]
            elif direction == Direction.right:
                if current.y + 1 > 7:
                    return None
                return self.board.nodes[current.x, current.y + 1]
        if current.y - 1 > -1:
            if current.f > self.board.nodes[current.x, current.y - 1].set_f():
                if current.y + 1 < 8:
                    if self.board.nodes[current.x, current.y + 1].set_f() > self.board.nodes[current.x, current.y - 1].f:
                        return self.board.nodes[current.x, current.y - 1]
                return self.board.nodes[current.x, current.y - 1]
        if current.y + 1 < 8:
            if current.f > self.board.nodes[current.x, current.y + 1].set_f():
                return self.board.nodes[current.x, current.y + 1]
        if rand:
            j = randrange(8)
            randresult = board.nodes[current.x, j]
            randresult.set_f()
            return randresult
        return None

    def cost(self):
        cost = 0
        for queen in queens:
            cost = cost + queen.set_f()
        return cost


e = 2.718281828
queens = []
red = f'{Colors.FAIL}{Colors.BOLD}'
green = f'{Colors.OKGREEN}{Colors.BOLD}'
yellow = f'{Colors.BOLD}{Colors.WARNING}'
end = f'{Colors.ENDC}{Colors.ENDC}'
board = Board()