from random import randrange


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

    def set_f(self, g):
        f = 0
        for i in range(0, x):
            if board.nodes[i, y].queen:
                f = f + 1
        for i in range(x + 1, 8):
            if board.nodes[i, y].queen:
                f = f + 1
        for j in range(0, y):
            if board.nodes[x, j].queen:
                f = f + 1
        for j in range(y + 1, 8):
            if board.nodes[x, j].queen:
                f = f + 1
        i = x - 1
        j = y - 1
        while i > 0 and j > 0:
            if board.nodes[i, j].queen:
                f = f + 1
            i = i - 1
            j = j - 1
        i = x - 1
        j = y + 1
        while i > 0 and j < 8:
            if board.nodes[i, j].queen:
                f = f + 1
            i = i - 1
            j = j + 1
        i = x + 1
        j = y - 1
        while i > 0 and j < 8:
            if board.nodes[i, j].queen:
                f = f + 1
            i = i + 1
            j = j - 1
        i = x + 1
        j = y + 1
        while i > 0 and j < 8:
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

    def __str__(self):
        return self.board.__str__()

queens = []
red = f'{Colors.FAIL}{Colors.BOLD}'
green = f'{Colors.OKGREEN}{Colors.BOLD}'
yellow = f'{Colors.BOLD}{Colors.WARNING}'
end = f'{Colors.ENDC}{Colors.ENDC}'
board = Board()