from copy import deepcopy
from typing import Type
from tictactoe.game import FieldState, Field


class Grid:

    def __init__(self):
        self.__grid = [[Type[Field] for x in range(3)] for y in range(3)]

    def populate(self):
        for y in range(3):
            for x in range(3):
                self.__grid[y][x] = Field(x, y, FieldState.NONE)

    def same_state(self, coordinates: [[int]], state: FieldState) -> bool:
        for coordinate in coordinates:
            if self.get_field(coordinate[0], coordinate[1]).state is not state:
                return False
        return True

    def is_full(self) -> bool:
        return len(list(filter(lambda f: f.state is FieldState.NONE, self.iterfields()))) == 0

    def is_empty(self) -> bool:
        return len(list(filter(lambda f: f.state is not FieldState.NONE, self.iterfields()))) == 0

    def set_field(self, x: int, y: int, s: FieldState):
        self.__grid[y][x].state = s

    def get_field(self, x: int, y: int) -> Field:
        return self.__grid[y][x]

    def iterfields(self, state: FieldState = None) -> [Field]:
        fields = []
        for y in range(3):
            fields = fields + self.__grid[y]
        return fields if state is None else list(filter(lambda f: f.state is state, fields))

    def clone(self) -> 'Grid':
        return deepcopy(self)

    def print_grid(self):
        print("-------------")
        for y in range(3):
            print("|", end="")
            for x in range(3):
                print(f" {self.get_field(x, y).state.value} |", end="")
            print("\n-------------")
