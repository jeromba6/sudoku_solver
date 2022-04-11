#!/bin/env python3
"""
Refined version of sudoku solver
"""

from sudoku import Sudoku
import ui

sudoku_challange ='''020480000
000009000
000002769
000970000
289000500
010200000
030000940
001690850
008120000'''

# sudoku_challange ='''123456789
# 123456789
# 123456789
# 123456789
# 123456789
# 123456789
# 123456789
# 123456789
# 123456789
# '''

def main():
    game = Sudoku(sudoku_challange)
    ui.output(game.board)
    print()

    while not game.solved():
        step, progress = game.solve_step_options()
        ui.output_options(step,game.board)
        if not progress:
            break
        game.solve_step(step)
        print()

    if game.solved():
        print('Game is solved')
    else:
        print('Not able to solve')
    ui.output(game.board,game.board_start)


if __name__ == '__main__':
    main()