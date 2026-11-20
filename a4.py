import math


# ========= PART A - Backtracking =========

# A1. Sudoku Solver
def parse(s:str):
    grid = []
    if len(s) != 81:
        raise ValueError("input must be 81 digits long to fill the board properly")
    for row in range(9):
        grid.append([int(s[row*9 + col]) for col in range(9)])
    return grid

def solve(grid, order="row"):

    def is_complete(grid):
        if grid.contains(0):
            return False
        else:
            return True
        
    def is_legal(grid, x_pos):
        if grid[x_pos[0]]
    """
    if grid is complete (contains no 0's)
        report it
        return True #found
    for each option x (1-9)
        if grid + x is legal
            placements += 1
            if solve(grid+x, placements):
                return grid,placements #Stop
    return False #backtrack
    """
    
    placements = 0
    solution = None
    if(order == "row"):
        pass
    elif(order == "fewest"):
        pass

    if(solution is None): 
        return None
    return (solution, placements)

def test_a1():
    P1 = ("014000356003000048050063100"
          "000002004305010090192047060"
          "407030005900006400500784200")
    P2 = ("091800000023050010500000000"
          "080003200070080006000001007"
          "800260105009305600010700090")
    P3 = ("000080040000200900160700000"
          "080090500020000000000006009"
          "907010002052000084006040000")
    P4 = ("714000356003000048050063100"
          "000002004305010090192047060"
          "407030005900006400500784200")
    #parse each example string from the pdf, run it in solve()
    #assert that results match expected from the pdf
    # print the solved grids for the report
    # print running time, order, and placements for 
    # each solve() call for a table in the report

#write explanation for the report on why "fewest" needs less placements

# A2. Certificate Check

def check_sudoku(puzzle, solution):
    #check that solution is 9x9 and contains only digits 1-9
    #every row, column, and 3x3 block contains 1-9 exactly once
    #solution agrees with every given puzzle
    
    return True

def test_a2():
    assert check_sudoku(P1,solve(parse(P1),order="row")[0])
    assert check_sudoku(P1,solve(parse(P1),order="fewest")[0])
    assert check_sudoku(P2,solve(parse(P2),order="row")[0])
    assert check_sudoku(P2,solve(parse(P2),order="fewest")[0])
    assert check_sudoku(P3,solve(parse(P3),order="row")[0])
    assert check_sudoku(P3,solve(parse(P3),order="fewest")[0])
    assert not check_sudoku(P4,solve(parse(P4),order="row")[0])
    assert not check_sudoku(P4,solve(parse(P4),order="fewest")[0])


# A3. N-Queens

def count_queens(n):
    #find all solutions to n_queens by backtracking
    squares_tested = 0
    solutions = 0
    return (solutions,squares_tested)

def test_a3():
    for n in range (4,13):
        #time count_queens(n)
        #print runtime, solutions, squares_tested, math.factorial(n)
        #explain the question in A3.3 for the writeup
        pass
    assert count_queens(8) ==(92,15720)

# ========= PART B - Branch and bound =========

# B1. 0/1 knapsack
def knapsack_bb(items, W, bound="simple"):
    return (best_value, take, boxes)

def knapsack_dp(items,W):
    #copy over from week 2 assignment
    pass

def test_b1():
    test_n = [10,20,30,40]
    for _ in test_n:
        for n in range(10):
            #make random instance
            #make correlated instance
            pass
        pass

# B2. TSP

def tsp_bb(D, bound="levitin"):
    return (length,tour,boxes,tours)

def test_b2():
    pass

# ========= PART C =========

# done by hand, images included in pdf writeup

if __name__ == "__main__":
    arr = parse("014000356003000048050063100"
          "000002004305010090192047060"
          "407030005900006400500784200")
    for row in arr:
        print(*row)