def output(board, start_board=None) -> None:
    ansi = {
        'normal': '\033[0m',
        'red':    '\033[31m',
        'green':  '\033[32m',
        'yellow': '\033[33m',
        'bold':   '\033[1m',
    }
    for x in range(9):
        if x > 1 and x % 3 ==0 : print('-'*15)
        for y in range(9):
            if y > 1 and y % 3 == 0:
                print(' | ', end='')
            val = board[x][y] if board[x][y] and int(board[x][y]) else ' '
            color = ansi['normal']
            if start_board:
                if start_board[x][y] in ('1','2','3','4','5','6','7','8','9'):
                    color = ansi['red']
            print(f'{color}{val}{ansi["normal"]}', end='')
        print()

def output_options(options,board) -> None:
    ansi = {
        'normal': '\033[0m',
        'red':    '\033[31m',
        'green':  '\033[32m',
        'yellow': '\033[33m',
        'bold':   '\033[1m',
    }
    color = ''
    for x in range(9):
        if x > 1 and x % 3 ==0 : print('-'*95)
        for y in range(9):
            if y > 1 and y % 3 == 0:
                print(' | ', end='')
            if board[x][y] != '0':
                color =  ansi['green']
            elif len(options[x][y]) == 1:
                color = ansi['yellow']
            else:
                color = ansi['red']
            val = options[x][y] if board[x][y] and int(options[x][y]) else ' '
            print(f'{color}{val: ^10}{ansi["normal"]}', end='')
        print()

