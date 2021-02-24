from tictactoe.game import FieldState


class Field:

    def __init__(self, x: int, y: int, s: FieldState):
        self.__x = x
        self.__y = y
        self.__state = s

    @property
    def x(self) -> int:
        return self.__x

    @property
    def y(self) -> int:
        return self.__y

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, value: FieldState):
        self.__state = value
