from pprint import pprint
import random
import copy

new_sudoku = [[-1 for col in range(9)] for row in range(9)]

def find_next_empty(puzzle):
    # finds the next row, col on puzzle that's not filled yet --> we represent these with -1
    # returns a row, col tuple (or (None, None) if there is none)
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1: 
                return row, col
    return None, None

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False
    row_arr = puzzle[row]
    if guess in row_arr:
        return False
    
    col_arr = []
    for i in range(9):
        col_arr.append(puzzle[i][col])
    if guess in col_arr:
        return False

    row_section = (row//3)*3
    col_section = (col//3)*3
    for j in range(row_section, row_section+3):
        for l in range(col_section, col_section+3):
            if guess == puzzle[j][l]: 
                return False

    return True
        
def solve_sudoku(puzzle):
    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return solution
    row, col = find_next_empty(puzzle)
    
    if row == None: 
        return True
    
    for p in range(1, 10):
        if is_valid(puzzle, p, row, col):
            puzzle[row][col] = p
            
            if solve_sudoku(puzzle):
                return True

        puzzle[row][col] = -1
            
    return False

def sudoku_generator():
    example_solution = [
            [3, 9, 1, 8, 5, 6, 4, 2, 7],
            [8, 6, 7, 2, 3, 4, 9, 1, 5],
            [4, 2, 5, 7, 1, 9, 6, 8, 3],
            
            [7, 5, 4, 9, 6, 8, 1, 3, 2],
            [2, 1, 6, 4, 7, 3, 5, 9, 8],
            [9, 3, 8, 5, 2, 1, 7, 6, 4],
            
            [5, 4, 3, 6, 9, 2, 8, 7, 1],
            [6, 7, 2, 1, 8, 5, 3, 4, 9],
            [1, 8, 9, 3, 4, 7, 2, 5, 6]
        ]
    
    swap_row(example_solution)
    swap_row_block(example_solution)
    swap_col(example_solution)
    swap_col_block(example_solution)
    #pprint(example_solution)
    
    return example_solution
    

def swap_row(puzzle):
    for x in range(3):
        order = [0+(x*3), 1+(x*3), 2+(x*3)]
        random.shuffle(order)  
        puzzle[0+(x*3)], puzzle[1+(x*3)], puzzle[2+(x*3)] = puzzle[order[0]], puzzle[order[1]], puzzle[order[2]]

def swap_row_block(puzzle):
    origin_order = [0, 3, 6]
    order = [0, 3, 6]
    random.shuffle(order) 
    
    for y in range(3):
        if origin_order[y] != order[y]:
            puzzle[origin_order[y]],\
            puzzle[origin_order[y]+1],\
            puzzle[origin_order[y]+2],\
            puzzle[order[y]],\
            puzzle[order[y]+1],\
            puzzle[order[y]+2] = \
                puzzle[order[y]],\
                puzzle[order[y]+1],\
                puzzle[order[y]+2],\
                puzzle[origin_order[y]],\
                puzzle[origin_order[y]+1],\
                puzzle[origin_order[y]+2]

def swap_col(puzzle):       
    for z in range(3):
        origin_order = [0+(z*3), 1+(z*3), 2+(z*3)]
        order = [0+(z*3), 1+(z*3), 2+(z*3)]
        random.shuffle(order)
                    
        first_col = [i[order[0]] for i in puzzle]
        second_col = [i[order[1]] for i in puzzle]
        third_col = [i[order[2]] for i in puzzle]
                
        for l in range(9):
            puzzle[l][origin_order[0]] = first_col[l]
            puzzle[l][origin_order[1]] = second_col[l]
            puzzle[l][origin_order[2]] = third_col[l]

def swap_col_block(puzzle):         
    origin_order = [0, 3, 6]
    order = [0, 3, 6]
    random.shuffle(order) 
    
    block1_first_col = [i[order[0]] for i in puzzle]
    block1_second_col = [i[order[0]+1] for i in puzzle]
    block1_third_col = [i[order[0]+2] for i in puzzle]
    block2_first_col = [i[order[1]] for i in puzzle]
    block2_second_col = [i[order[1]+1] for i in puzzle]
    block2_third_col = [i[order[1]+2] for i in puzzle]
    block3_first_col = [i[order[2]] for i in puzzle]
    block3_second_col = [i[order[2]+1] for i in puzzle]
    block3_third_col = [i[order[2]+2] for i in puzzle]
    
    for l in range(9):
        puzzle[l][origin_order[0]] = block1_first_col[l]
        puzzle[l][origin_order[0]+1] =  block1_second_col[l]
        puzzle[l][origin_order[0]+2] = block1_third_col[l]
        puzzle[l][origin_order[1]] = block2_first_col[l]
        puzzle[l][origin_order[1]+1] = block2_second_col[l]
        puzzle[l][origin_order[1]+2] = block2_third_col[l]
        puzzle[l][origin_order[2]] = block3_first_col[l]
        puzzle[l][origin_order[2]+1] = block3_second_col[l]
        puzzle[l][origin_order[2]+2] = block3_third_col[l]

def get_non_empty_squares(puzzle):
    row = []
    col = []
    for x in range(81):
        r=x//9
        c=x%9
        if puzzle[r][c] > 0:
            row.append(r)
            col.append(c) 
    return row, col
        
def create_puzzle(puzzle):
    """remove numbers from the puzzle to create the puzzle"""
    #get all non-empty squares from the puzzle
    non_empty_squares_row, non_empty_squares_col = get_non_empty_squares(puzzle)
    non_empty_squares_count = len(non_empty_squares_row)
    
    while non_empty_squares_count >= 28:
        #there should be at least 17 clues
        random_number = random.randint(0, non_empty_squares_count-1)
        row = non_empty_squares_row.pop(random_number)
        col = non_empty_squares_col.pop(random_number)
        non_empty_squares_count -= 1
        #might need to put the square value back if there is more than one solution
        removed_square = puzzle[row][col]
        puzzle[row][col] = -1
        
    return puzzle
    
'''if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    
    #x = sudoku_generator()
    #print(solve_sudoku(example_board))
    #pprint(example_board)
    
    #print(sudoku_generator())
    #print(get_non_empty_squares(example_board))
    #pprint(create_puzzle(x))
    #print(solve_sudoku(x))
    #pprint(x)
    '''
    
    