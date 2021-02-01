from os import system
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


class Nut(Enum):
    """There are two Nuts in the game, one X and one O"""
    X = 0
    O = 1


class Node:
    """Every node in 3x3 board is an object of Node Class"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.nut = None
        self.green = False
    
    def get_nut_str(self):
        if self.nut == Nut.X:
            if self.green:
                return f'{green}X{end}'
            return f'{yellow}X{end}'
        elif self.nut == Nut.O:
            if self.green:
                return f'{green}O{end}'
            return f'{red}O{end}'
        else:
            return ' '

    def set_green(self):
        if self.green:
            self.green = False
        else:
            self.green = True
    
    def __str__(self):
        return f'x = {self.x} - y = {self.y} - nut = {self.get_nut_str()} - green = {self.green}'


class Board:
    """The board that has a 3x3 plane to play"""
    def __init__(self):
        self.nodes = {}
        self.turn = Nut.O
        for i in range(3):
            for j in range(3):
                self.nodes[i, j] = Node(i, j)
    
    def switch_turn(self):
        if self.turn == Nut.X:
            self.turn = Nut.O
        elif self.turn == Nut.O:
            self.turn = Nut.X

    def play(self, node):
        if node.nut != None:
            return False
        if self.turn == Nut.X:
            node.nut = Nut.X
        else:
            node.nut = Nut.O
        self.switch_turn()
        return True

    def unplay(self, node):
        self.switch_turn()
        node.nut = None

    def possible_actions(self):
        allowed = []
        for i in range(3):
            for j in range(3):
                if not self.nodes[i, j].nut:
                    allowed.append(self.nodes[i, j])
        return allowed

    def copy_board(self, board):
        for i in range(3):
            for j in range(3):
                self.nodes[i, j].nut = board.nodes[i, j].nut
        self.turn = board.turn

    def score(self):
        score = 0
        for i in range(3):
            if self.nodes[i, 0].nut != Nut.O and self.nodes[i, 1].nut != Nut.O and self.nodes[i, 2].nut != Nut.O:
                score = score + 1
        for j in range(3):
            if self.nodes[0, j].nut != Nut.O and self.nodes[1, j].nut != Nut.O and self.nodes[2, j].nut != Nut.O:
                score = score + 1
        if self.nodes[0, 0].nut != Nut.O and self.nodes[1, 1].nut != Nut.O and self.nodes[2, 2].nut != Nut.O:
            score = score + 1
        if self.nodes[0, 2].nut != Nut.O and self.nodes[1, 1].nut != Nut.O and self.nodes[2, 0].nut != Nut.O:
            score = score + 1
        return score
    
    def negative_score(self):
        score = 0
        for i in range(3):
            if self.nodes[i, 0].nut != Nut.X and self.nodes[i, 1].nut != Nut.X and self.nodes[i, 2].nut != Nut.X:
                score = score + 1
        for j in range(3):
            if self.nodes[0, j].nut != Nut.X and self.nodes[1, j].nut != Nut.X and self.nodes[2, j].nut != Nut.X:
                score = score + 1
        if self.nodes[0, 0].nut != Nut.X and self.nodes[1, 1].nut != Nut.X and self.nodes[2, 2].nut != Nut.X:
            score = score + 1
        if self.nodes[0, 2].nut != Nut.X and self.nodes[1, 1].nut != Nut.X and self.nodes[2, 0].nut != Nut.X:
            score = score + 1
        return score

    def status(self):
        for i in range(3):
            j = 0
            if self.nodes[i, j].nut == self.nodes[i, j + 1].nut and self.nodes[i, j].nut == self.nodes[i, j + 2].nut and self.nodes[i, j].nut != None:
                if self.nodes[i, j] == Nut.X:
                    return self.winner_message(Nut.X, [[i, j], [i, j + 1], [i, j + 2]])
                else:
                    return self.winner_message(Nut.O, [[i, j], [i, j + 1], [i, j + 2]])
        for j in range(3):
            i = 0
            if self.nodes[i, j].nut == self.nodes[i + 1, j].nut and self.nodes[i, j].nut == self.nodes[i + 2, j].nut and self.nodes[i, j].nut != None:
                if self.nodes[i, j] == Nut.X:
                    return self.winner_message(Nut.X, [[i, j], [i + 1, j], [i + 2, j]])
                else:
                    return self.winner_message(Nut.O, [[i, j], [i + 1, j], [i + 2, j]])
        if self.nodes[0, 0].nut == self.nodes[1, 1].nut and self.nodes[0, 0].nut == self.nodes[2, 2].nut and self.nodes[0, 0].nut != None:
            if self.nodes[0, 0].nut == Nut.X:
                return self.winner_message(Nut.X, [[0, 0], [1, 1], [2, 2]])
            else:
                return self.winner_message(Nut.O, [[0, 0], [1, 1], [2, 2]])
        if self.nodes[0, 2].nut == self.nodes[1, 1].nut and self.nodes[0, 2].nut == self.nodes[2, 0].nut and self.nodes[0, 2].nut != None:
            if self.nodes[0, 2].nut == Nut.X:
                return self.winner_message(Nut.X, [[0, 2], [1, 1], [2, 0]])
            else:
                return self.winner_message(Nut.O, [[0, 2], [1, 1], [2, 0]])
        return self.winner_message(None, None)
    
    def winner_message(self ,nut, positions):
        if nut:
            for position in positions:
                self.nodes[position[0], position[1]].set_green()
            if Nut.X == nut:
                system('clear')
                print(f'{green}We Got A Winner Who Is {end}{red}X{end}{green} Player{end}')
                print(self)
                return [True]
            if Nut.O == nut:
                system('clear')
                print(f'{green}We Got A Winner Who Is {end}{red}O{end}{green} Player{end}')
                print(self)
                return [True]
        return [False]

    def __str__(self):
        rl = ['']*3
        for i in range(3):
            for j in range(3):
                if j == 0:
                    rl[i] = rl[i] + self.nodes[i, j].get_nut_str()
                elif j == 1:
                    rl[i] = rl[i] + f'{cyan}|{end}' + self.nodes[i, j].get_nut_str() + f'{cyan}|{end}'
                elif j == 2:
                    rl[i] = rl[i] + self.nodes[i, j].get_nut_str() + '\n'
        middle = f'{cyan}-+-+-{end}\n'
        output = ''
        for i in range(3):
            if i == 2:
                output = output + rl[i]
                return output
            output = output + rl[i] + middle


class Environment:
    """The class that has access to everything and actually solves the problem"""
    def __init__(self):
        self.board = board
    
    def __str__(self):
        return self.board.__str__()
    
    def start_game(self):
        while not self.board.status()[0]:
            system('clear')
            print(self.board)
            if self.board.turn == Nut.X:
                if not self.board.possible_actions():
                    break
                while True:
                    x = int(input('X = '))
                    y = int(input('Y = '))
                    if x >= 0 and x <= 2 and y >=0 and y <= 2:
                        if self.board.play(self.board.nodes[x, y]):
                            break
                        else:
                            print('please insert true values to play')
            else:
                bestNode = None
                best = -10000
                board = Board()
                board.copy_board(self.board)
                for node in board.possible_actions():
                    board.play(node)
                    maximum = self.minimum(board, 1, 3, best)
                    if best < maximum:
                        best = maximum
                        bestNode = node
                    board.unplay(node)
                if not board.possible_actions():
                    break
                self.board.play(self.board.nodes[bestNode.x, bestNode.y])
    
    def minimum(self, board, depth, depthLimit, alpha):
        if depthLimit == depth or board.possible_actions():
            return board.negative_score() - board.score()
        best = 10000
        for node in board.possible_actions():
            board.play(node)
            minimum = self.maximum(board, depth + 1, 5, best)
            if best > minimum:
                best = minimum
            board.unplay(node)
            if beta < best:
                return best
        return best

    def maximum(self, board, depth, depthLimit, beta):
        if depthLimit == depth or board.possible_actions():
            return board.score() - board.negative_score()
        best = -10000
        for node in board.possible_actions():
            board.play(node)
            maximum = self.minimum(board, depth + 1, 5, best)
            if best < maximum:
                best = maximum
            board.unplay(node)
            if alpha > best:
                return best
        return best


red = f'{Colors.FAIL}{Colors.BOLD}'
green = f'{Colors.OKGREEN}{Colors.BOLD}'
yellow = f'{Colors.BOLD}{Colors.WARNING}'
cyan = f'{Colors.OKCYAN}{Colors.BOLD}'
end = f'{Colors.ENDC}{Colors.ENDC}'
board = Board()