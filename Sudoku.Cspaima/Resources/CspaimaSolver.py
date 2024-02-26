from timeit import default_timer
from constraint import Problem, AllDifferentConstraint

#instance = [[0,0,0,0,9,4,0,3,0],
#           [0,0,0,5,1,0,0,0,7],
#           [0,8,9,0,0,0,0,4,0],
#           [0,0,0,0,0,0,2,0,8],
#           [0,6,0,2,0,1,0,5,0],
#           [1,0,2,0,0,0,0,0,0],
#          [0,7,0,0,0,0,5,2,0],
#          [9,0,0,0,6,5,0,0,0],
#          [0,4,0,9,7,0,0,0,0]]


def solve_sudoku_csp(grid):
    sudoku_size = 9
    block_size = 3

    problem = Problem()

    # Add variables for each cell
    for i in range(sudoku_size):
        for j in range(sudoku_size):
            problem.addVariable((i, j), range(1, sudoku_size + 1))

    # Add constraints for rows and columns
    for i in range(sudoku_size):
        problem.addConstraint(AllDifferentConstraint(), [(i, j) for j in range(sudoku_size)])  # All values in a row must be different
        problem.addConstraint(AllDifferentConstraint(), [(j, i) for j in range(sudoku_size)])  # All values in a column must be different

    # Add constraints for blocks
    for i in range(block_size):
        for j in range(block_size):
            block_cells = [(r, c) for r in range(i * block_size, (i + 1) * block_size) for c in range(j * block_size, (j + 1) * block_size)]
            problem.addConstraint(AllDifferentConstraint(), block_cells)  # All values in a block must be different

    # Add constraints for given values
    for i in range(sudoku_size):
        for j in range(sudoku_size):
            if grid[i][j] != 0:
                problem.addConstraint(lambda var, val=grid[i][j]: var == val, [(i, j)])  # Assign given values

    # Solve the Sudoku
    solution = problem.getSolution()

    if solution:
        result = [[solution[(i, j)] for j in range(9)] for i in range(9)]
        return True, result  # Indique qu'une solution a été trouvée et la renvoie
    else:
        return False, None  # Indique qu'aucune solution n'a été trouvée



# Appel de la fonction pour résoudre le Sudoku
solution_found, instance = solve_sudoku_csp(instance)

if solution_found:
        # print("Solution trouvée :")
   # for row in solved_instance:
   #     print(" ".join(map(str, row)))
        r=instance
else:
    print("Aucune solution trouvée.")