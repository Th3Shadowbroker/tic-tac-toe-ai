from tictactoe.game import FieldState
from tictactoe.game.player import AbstractPlayer


class Player(AbstractPlayer):

    def play(self):
        self.__request_input()

    def __request_input(self) -> (int, int):
        user_input = None

        try:
            user_input = input("Select a field (1-9): ")
        except KeyboardInterrupt:
            print("Bye!")
            exit()

        if user_input.isnumeric():
            field_index = int(user_input) - 1
            if 0 <= field_index < 9:
                from tictactoe import Game
                field = Game.get_instance().grid.iterfields()[field_index]
                if field.state is FieldState.NONE:
                    field.state = FieldState.PLAYER
                else:
                    print("This field is already occupied :/")
                    self.__request_input()
            else:
                print("That's not what I meant by breaking the boundaries!")
                self.__request_input()
        else:
            print(f"'{user_input}' is not a number!")
            self.__request_input()
