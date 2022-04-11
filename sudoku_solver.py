#!/usr/bin/env python3

sudoku='''020480000
000009000
000002769
000970000
289000500
010200000
030000940
001690850
008120000'''

# sudoku='''008400002
# 000900003
# 207000450
# 000209706
# 009000508
# 005806000
# 046000305
# 300007000
# 800004600'''

# #Hardest to solve
# sudoku='''800000000
# 003600000
# 070090200
# 050007000
# 000045700
# 000100030
# 001000068
# 008500010
# 090000400'''

# sudoku='''001058060
# 800016050
# 520700100
# 000001023
# 082060410
# 600900000
# 008007500
# 040600002
# 050120800'''

# sudoku='''005073060
# 040960000
# 000000240
# 000030400
# 000080001
# 000210530
# 400000003
# 056000009
# 908700000'''


def read_sudoku(input):
    output = []
    for linenr, line in enumerate(input.split()):
        output.append([char for char in line])
    return output

def options_row_colum_block(input):
    output=[]
    for i in range(9):
        output.append([])
        for j in range(9):
            output[i].append(valid_values(i,j,input))
    return output

def valid_values(x,y,input):
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

def print_step(sudoku, options):
    for x in range(9):
        if x > 1 and x % 3 ==0: print('-'*95)
        for y in range(9):
            if y > 1 and y % 3 ==0: print('| ', end='')
            if sudoku[x][y] == '0':
                val = options[x][y]
                if len(val) == 1:
                    val = '#' + val + '#'
            else:
                val = options[x][y]
            print('{:^10}'.format(val), end='')
        print()

def block_single_valid(options):
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

def block_row_col(options):
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

def set_options(sudoku, options):
    changed = False
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == '0'  and len(options[x][y]) == 1:
                if sudoku[x][y] != options[x][y]:
                    changed = True
                    sudoku[x][y] = options[x][y]
    return sudoku, changed

def sudoku_guess(input):
    print('guessing')
    pass
    # Find entries with least prosible option > 1
    # chose 1 return and continue

sudoku_step1 = read_sudoku(sudoku)
guessing = True
continue_loop = True
loop_count = 0
guess = []
guess_count = 0
guesses = 0
while continue_loop:
    restart = False
    loop_count += 1
    print('Loopcount: {}'.format(str(loop_count)))
    sudoku_options = options_row_colum_block(sudoku_step1)
    sudoku_options = block_single_valid(sudoku_options)
    sudoku_options = block_row_col(sudoku_options)
    sudoku_options = block_single_valid(sudoku_options)
    print_step(sudoku_step1,sudoku_options)
    if len(guess) != 0:
        for I in range(81):
            x = I % 9
            y = I // 9
            if len(sudoku_options[x][y]) == 0:
                print()
                restart = True
                guess_count = 0
                sudoku_options = []
                sudoku_step1 = read_sudoku(sudoku)
                break
    if not restart:
        sudoku_step1, change = set_options(sudoku_step1, sudoku_options)
    else:
        restart = False
        continue
    if change:
        print()
    else:
        if not guessing:
            print('Sorry was not able to solve this one')
            break
        found = False
        mustbreak = False
        for i in range(2,9):
            for j in range(81):
                x = j % 9
                y = j // 9

                # Find first avalible cell with least options
                if len(sudoku_options[x][y]) == i:
                    # When true this is a new option
                    if len(guess) == guess_count:
                        guesses += 1
                        guess.append(0)
                        found = True
                        guess_count += 1
                        break

                    # This option is used before
                    else:
                        # Are all posible options used for this cell?
                        if guess[guess_count] + 1 < len(sudoku_options[x][y]):
                            guess[guess_count] += 1
                            guess_count += 1
                            guess = guess[:guess_count+1]
                            found = True
                            break
                        else:
                            sudoku_step1[x][y] = sudoku_options[x][y][guess[guess_count]]
                            guess_count += 1
                            mustbreak = True
                            break
            if mustbreak:
                break
            if found:
                sudoku_options[x][y] = sudoku_options[x][y][guess[guess_count-1]]
                sudoku_step1, change = set_options(sudoku_step1, sudoku_options)
                break

    for i in range(81):
        x = i % 9
        y = i // 9
        if sudoku_step1[x][y] == '0':
            break
        if i == 80:
            continue_loop = False
            print('### Final solution is: ###')
            print('Guesses needed to solve: {}'.format(guesses))
            print_step(sudoku_step1,sudoku_options)
