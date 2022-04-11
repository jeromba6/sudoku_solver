import copy

class Sudoku():
    def __init__(self, chalange: str) -> None:
        self.board = []
        for line in chalange.split():
            self.board.append([char for char in line])
        self.board_start = copy.deepcopy(self.board)


    def solved(self):
        '''
        Is the Sudoku solved, determine by getting the minimal value on the board.
        This should not be 0
        '''
        return bool(min([min(set(map(int,r))) for r in self.board]))


    def solve_step_options(self):
        sudoku_options = options_row_colum_block(self.board)
        sudoku_options = block_single_valid(sudoku_options)
        sudoku_options = block_row_col(sudoku_options)
        sudoku_options = block_single_valid(sudoku_options)
        return sudoku_options, self.progress(sudoku_options)


    def progress(self, sudoku_options) -> bool:
        for i in range(81):
            x = i // 9
            y = i % 9
            if int(self.board[x][y]):
                continue
            if len(sudoku_options[x][y]) == 1:
                return True
        return False


    def solve_step(self, options) -> None:
        for i in range(81):
            x = i // 9
            y = i % 9
            if int(self.board[x][y]):
                continue
            if len(options[x][y]) == 1:
                self.board[x][y] = options[x][y]


    def solve_complete(self) -> bool:
        raise NotImplemented


def block_single_valid(options) -> list:
    for b in range(9):
        bx = (b % 3) * 3
        by = (b // 3) * 3
        for c in range(8):
            cx = c % 3
            cy = c // 3
            lval = [c]
            for cc in range(c + 1,9):
                ccx = cc % 3
                ccy = cc // 3
                if options[bx + cx][by + cy] == options[bx + ccx][by + ccy]:
                    lval.append(cc)
            if len(options[bx + cx][by + cy]) == len(lval):
                for cc in range(9):
                    if not cc in lval:
                        for rem_val in options[bx + cx][by + cy]:
                            ccx = cc % 3
                            ccy = cc // 3
                            options[bx + ccx][by + ccy] = options[bx + ccx][by + ccy].replace(rem_val,'')
    for b in range(9):
        bx = b % 3
        by = b // 3
        for c in range(9):
            x = bx * 3 + c % 3
            y = by * 3 + (c // 3)
            if len(options[x][y]) > 1:
                for val in options[x][y]:
                    single_valid = True
                    for cc in range(9):
                        cx = bx * 3 + cc % 3
                        cy = by * 3 + (cc // 3)
                        if x != cx or y != cy:
                            if val in options[cx][cy]:
                                single_valid =  False
                                break
                    if single_valid:
                        options[x][y] = val
                        break
    return options

def block_row_col(options) -> list:
    for b in range(9):
        bx = b % 3
        by = b // 3
        for val in range(1,10):
            valy=[]
            for y in range(3):
                for x in range(3):
                    if str(val) in options[bx*3 + x][by*3 + y]:
                        valy.append(y)
                        break
            if len(valy) == 1:
                for obx in range(3):
                    if obx != bx:
                        for x in range(3):
                            cx = obx * 3 + x
                            cy = by * 3 + valy[0]
                            options[cx][cy] = options[cx][cy].replace(str(val),'')

            valx=[]
            for x in range(3):
                for y in range(3):
                    if str(val) in options[bx*3 + x][by*3 + y]:
                        valy.append(x)
                        break
            if len(valx) == 1:
                for oby in range(3):
                    if oby != by:
                        for y in range(3):
                            cx = bx * 3 + valx[0]
                            cy = oby * 3 + y
                            options[cx][cy] = options[cx][cy].replace(str(val),'')
    return options



def options_row_colum_block(input) -> list:
    output=[]
    for i in range(9):
        output.append([])
        for j in range(9):
            output[i].append(valid_values(i,j,input))
    return output


def row_colum_block(options) -> list:
    for b in range(9):
        bx = b % 3
        by = b // 3
        for val in range(1,10):
            valy=[]
            for y in range(3):
                for x in range(3):
                    if str(val) in options[bx*3 + x][by*3 + y]:
                        valy.append(y)
                        break
            if len(valy) == 1:
                for obx in range(3):
                    if obx != bx:
                        for x in range(3):
                            cx = obx * 3 + x
                            cy = by * 3 + valy[0]
                            options[cx][cy] = options[cx][cy].replace(str(val),'')

            valx=[]
            for x in range(3):
                for y in range(3):
                    if str(val) in options[bx*3 + x][by*3 + y]:
                        valy.append(x)
                        break
            if len(valx) == 1:
                for oby in range(3):
                    if oby != by:
                        for y in range(3):
                            cx = bx * 3 + valx[0]
                            cy = oby * 3 + y
                            options[cx][cy] = options[cx][cy].replace(str(val),'')
    return options


def valid_values(x,y,input) -> str:
    if input[x][y] == '0':
        bx = x // 3
        by = y // 3
        valid="123456789"
        for i in range(9):
            valid=valid.replace(input[i][y], '')
            valid=valid.replace(input[x][i], '')
            cx = bx * 3 + (i // 3)
            cy = by * 3 + (i % 3)
            valid=valid.replace(input[cx][cy],'')
    else:
        return input[x][y]
    return valid