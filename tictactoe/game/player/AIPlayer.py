from tictactoe.game import FieldState, Grid, Turn
from tictactoe.game.player import AbstractPlayer
from tictactoe.util import GridUtil
from math import inf
from random import randint


class AIPlayer(AbstractPlayer):

    __counter = 0

    def play(self):
        from tictactoe import Game
        game = Game.get_instance()

        if game.grid.is_empty():
            field_index = randint(0, 8)
            game.grid.iterfields()[field_index].state = FieldState.BOT
        else:
            best_move = self.minimax(game.grid, len(game.grid.iterfields(FieldState.NONE)), Turn.BOT)
            print(best_move)
            game.grid.set_field(best_move[0], best_move[1], FieldState.BOT)
            print(f"Evaluated {self.__counter} scenarios!")
            self.__counter = 0

    def evaluate(self, grid: Grid) -> int:
        if GridUtil.bot_won(grid):
            return 1
        elif GridUtil.player_won(grid):
            return -1
        else:
            return 0

    def minimax(self, grid: Grid, depth: int, turn: Turn) -> [int, int, int]:
        self.__counter = self.__counter + 1
        best_score = [-1, -1, -inf if turn is Turn.BOT else inf]

        if depth == 0:
            return [-1, -1, self.evaluate(grid)]

        for field in grid.iterfields(FieldState.NONE):
            grid.set_field(field.x, field.y, FieldState.PLAYER if turn is Turn.PLAYER else FieldState.BOT)
            score = self.minimax(grid, depth - 1, Turn.PLAYER if turn is Turn.BOT else Turn.BOT)
            grid.set_field(field.x, field.y, FieldState.NONE)
            score[0], score[1] = field.x, field.y

            if turn is Turn.BOT:
                if score[2] > best_score[2]:
                    best_score = score
            else:
                if score[2] < best_score[2]:
                    best_score = score
        return best_score
