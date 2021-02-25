import platform
from os import system
from tictactoe.game import Grid, Turn
from tictactoe.game.player import AIPlayer, Player
from tictactoe.util import GridUtil


class Game:

    __instance = None

    def __init__(self):
        Game.__instance = self

        self.__grid = Grid()
        self.__player = Player()
        self.__bot = AIPlayer()
        self.__turn = Turn.random()

    def start(self):
        self.__grid.populate()

        print(f"The {self.__turn.name.lower()} will make the first move!")
        self.__grid.print_grid()

        while (not GridUtil.player_won(self.__grid)) and (not GridUtil.bot_won(self.__grid)) and (not GridUtil.is_tied(self.__grid)):
            if self.__turn is Turn.PLAYER:
                self.__player.play()
            else:
                self.__bot.play()

            self.__grid.print_grid()
            self.__turn = Turn.PLAYER if self.__turn is Turn.BOT else Turn.BOT

        if GridUtil.player_won(self.__grid):
            print("The player won!")
        elif GridUtil.bot_won(self.__grid):
            print("The bot won!")
        else:
            print("Tie game!")

    def __clear_console(self):
        os_name = platform.system().lower()
        if 'windows' in os_name:
            system('cls')
        else:
            system('clear')

    @property
    def grid(self) -> Grid:
        return self.__grid

    @property
    def player(self) -> Player:
        return self.__player

    @property
    def ai(self) -> AIPlayer:
        return self.__bot

    @staticmethod
    def get_instance() -> 'Game':
        return Game.__instance
