"""
Author: Ty Klabacka

This function accepts a 2D array representing a Sudoku board, and returns true 
if it is a valid solution, or false otherwise. The cells of the sudoku 
board may also contain 0's, which will represent empty cells. Boards 
containing one or more zeroes are considered to be invalid solutions.
"""

def valid_solution(board):
    master = []
    for lst in board:
        if 0 in lst: return False
        else:
            master.append(lst)
    start, fin = 0, 3
    while fin <= 9:
        row_start, row_fin = 0, 3
        while row_fin <= 9:
            lyst = []
            for row in board[start:fin]:
                for col in row[row_start:row_fin]: lyst.append(col)
            master.append(lyst)
            row_start += 3
            row_fin += 3
        start += 3
        fin += 3
    for i in range(len(board)):
        column = []
        for row in board:
            column.append(row[i])
        master.append(column)
    check_lst = [0 if sorted(num) == [1,2,3,4,5,6,7,8,9] else 1 for num in master]
    if 1 in check_lst: return False
    else: return True











