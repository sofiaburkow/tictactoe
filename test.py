from tictactoe import create_new_board, game_finished, full_board

if __name__ == '__main__':
    board = create_new_board()
    assert game_finished(board) == False, f'Expected board to be finished: {board}'

    actually_finished_board = [
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
        ['O', 'O', 'O'],
    ]
    assert game_finished(actually_finished_board)

    actually_finished_board = [
        ['O', 'X', 'O'],
        ['O', 'X', ' '],
        ['O', ' ', 'X'],
    ]
    assert game_finished(actually_finished_board)

    assert full_board([
        ['O', 'X', 'O'],
        ['O', 'X', 'O'],
        ['O', 'X', 'X'],
    ])

    assert not full_board([
        ['O', 'X', 'O'],
        ['O', ' ', 'O'],
        ['O', 'X', 'X'],
    ])

    
    
