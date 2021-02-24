from tictactoe import Game
from tictactoe.game import FieldState

game = Game()

game.grid.populate()

game.grid.set_field(1, 1, FieldState.BOT)
game.grid.set_field(0, 1, FieldState.BOT)
game.grid.set_field(2, 1, FieldState.BOT)


grid1 = game.grid
grid2 = game.grid.clone()

grid2.set_field(1, 2, FieldState.PLAYER)

grid1.print_grid()
grid2.print_grid()
