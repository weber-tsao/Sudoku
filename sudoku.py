from pprint import pprint

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
    
if __name__ == '__main__':
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
    print(solve_sudoku(example_board))
    pprint(example_board)