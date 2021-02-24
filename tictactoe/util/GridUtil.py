from tictactoe.game import FieldState, Grid


class GridUtil:

    __constellations = [

            # Horizontal
            [[0, 0], [1, 0], [2, 0]],
            [[0, 1], [1, 1], [2, 1]],
            [[0, 2], [1, 2], [2, 2]],

            # Vertical
            [[0, 0], [0, 1], [0, 2]],
            [[1, 0], [1, 1], [1, 2]],
            [[2, 0], [2, 1], [2, 2]],

            # Diagonal
            [[0, 0], [1, 1], [2, 2]],
            [[2, 0], [1, 1], [0, 2]]

        ]

    @staticmethod
    def __wins(grid: Grid, state: FieldState) -> bool:
        for constellation in GridUtil.__constellations:
            if grid.same_state(constellation, state):
                return True

        return False

    @staticmethod
    def player_won(grid: Grid) -> bool:
        return GridUtil.__wins(grid, FieldState.PLAYER)

    @staticmethod
    def bot_won(grid: Grid) -> bool:
        return GridUtil.__wins(grid, FieldState.BOT)

    @staticmethod
    def is_tied(grid: Grid) -> bool:
        return (not GridUtil.player_won(grid)) and (not GridUtil.bot_won(grid)) and grid.is_full()
