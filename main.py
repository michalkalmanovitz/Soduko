################################################################
# ----------------------- handling board -----------------------
################################################################
def CreatingBoard(matrix_size):
    matrix = []
    for i in range(matrix_size):
        matrix.append([])
        for j in range(matrix_size):
            matrix[i].append(j)
    return matrix
def print_table(matrix, matrix_size):
    print("\n-----------------board:-----------------\n")
    board = ""
    for i in range(matrix_size):
        board += "\t"
        for j in range(matrix_size):
            board += str(matrix[i][j]) + "\t"
        board += "\n"
    print(board)

################################################################
# ---------------------- existing tests  -----------------------
################################################################
#passing on each row check if num init
def is_num_in_row(matrix, row, num):
    if num in matrix[row]:
        return True
    return False


# passing on each row, and fixed column check if num init
def is_num_in_column(matrix, column, num):
    for i in range(matrix_size):
        if matrix[i][column] == num:
            return True
    return False
################################################################
# ---------------------------- main ----------------------------
################################################################
# receive size of matrix
matrix_size = input("Enter size of matrix: ")
while not matrix_size.isdigit():
    matrix_size = input("INVALID AMOUNT. Enter size of matrix: ")

matrix_size = int(matrix_size)
matrix = CreatingBoard(matrix_size)
print_table(matrix, matrix_size)