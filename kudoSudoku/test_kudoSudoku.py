from kudoSudoku import sudoku
two = [[0, 2, 4, 0], [1, 0, 0, 3], [4, 0, 0, 2], [0, 1, 3, 0]]
easy = [[0, 7, 0, 0, 8, 4, 9, 0, 0], [1, 0, 0, 6, 0, 2, 0, 0, 0], [4, 0, 0, 0, 0, 0, 8, 0, 0], [0, 0, 9, 1, 0, 0, 0, 0, 2], [2, 0, 0, 0, 0, 0, 0, 0, 8], [3, 0, 0, 0, 0, 8, 6, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0, 5], [0, 0, 0, 4, 0, 1, 0, 0, 9], [0, 0, 1, 5, 6, 0, 0, 7, 0]]
medium = [[3, 0, 8, 0, 0, 0, 0, 0, 4], [9, 5, 0, 4, 0, 0, 0, 0, 0], [0, 4, 0, 0, 0, 8, 0, 5, 0], [4, 8, 0, 7, 0, 3, 0, 0, 0], [0, 0, 2, 0, 1, 0, 6, 0, 0], [0, 0, 0, 6, 0, 9, 0, 8, 2], [0, 2, 0, 5, 0, 0, 0, 3, 0], [0, 0, 0, 0, 0, 1, 0, 4, 6], [8, 0, 0, 0, 0, 0, 2, 0, 7]]
hard = [[8, 5, 0, 0, 0, 9, 0, 0, 2], [9, 0, 0, 0, 0, 0, 0, 5, 0], [0, 0, 6, 0, 8, 0, 0, 0, 7], [0, 0, 0, 5, 0, 0, 2, 8, 0], [0, 0, 0, 9, 0, 1, 0, 0, 0], [0, 2, 7, 0, 0, 4, 0, 0, 0], [7, 0, 0, 0, 3, 0, 8, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 3], [5, 0, 0, 6, 0, 0, 0, 2, 4]]
evil = [[0, 4, 0, 8, 0, 7, 0, 0, 0], [2, 0, 0, 0, 9, 0, 0, 0, 7], [0, 9, 0, 4, 0, 0, 0, 0, 3], [0, 8, 0, 0, 0, 0, 0, 0, 0], [7, 5, 0, 0, 2, 0, 0, 1, 8], [0, 0, 0, 0, 0, 0, 0, 7, 0], [5, 0, 0, 0, 0, 1, 0, 6, 0], [9, 0, 0, 0, 7, 0, 0, 0, 5], [0, 0, 0, 2, 0, 5, 0, 4, 0]]
mostEvil = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 3, 0, 8, 5], [0, 0, 1, 0, 2, 0, 0, 0, 0], [0, 0, 0, 5, 0, 7, 0, 0, 0], [0, 0, 4, 0, 0, 0, 1, 0, 0], [0, 9, 0, 0, 0, 0, 0, 0, 0], [5, 0, 0, 0, 0, 0, 0, 7, 3], [0, 0, 2, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 4, 0, 0, 0, 9]]

mediums = [[3, 6, 8, 9, 7, 5, 1, 2, 4], [9, 5, 1, 4, 3, 2, 7, 6, 8], [2, 4, 7, 1, 6, 8, 3, 5, 9], [4, 8, 6, 7, 2, 3, 9, 1, 5], [5, 9, 2, 8, 1, 4, 6, 7, 3], [1, 7, 3, 6, 5, 9, 4, 8, 2], [6, 2, 4, 5, 9, 7, 8, 3, 1], [7, 3, 9, 2, 8, 1, 5, 4, 6], [8, 1, 5, 3, 4, 6, 2, 9, 7]]
evils = [[3, 4, 5, 8, 6, 7, 2, 9, 1], [2, 6, 1, 5, 9, 3, 4, 8, 7], [8, 9, 7, 4, 1, 2, 6, 5, 3], [1, 8, 9, 7, 5, 6, 3, 2, 4], [7, 5, 6, 3, 2, 4, 9, 1, 8], [4, 3, 2, 1, 8, 9, 5, 7, 6], [5, 7, 3, 9, 4, 1, 8, 6, 2], [9, 2, 4, 6, 7, 8, 1, 3, 5], [6, 1, 8, 2, 3, 5, 7, 4, 9]]
hards = [[8, 5, 3, 7, 1, 9, 6, 4, 2], [9, 7, 1, 2, 4, 6, 3, 5, 8], [2, 4, 6, 3, 8, 5, 9, 1, 7], [4, 6, 9, 5, 7, 3, 2, 8, 1], [3, 8, 5, 9, 2, 1, 4, 7, 6], [1, 2, 7, 8, 6, 4, 5, 3, 9], [7, 9, 4, 1, 3, 2, 8, 6, 5], [6, 1, 2, 4, 5, 8, 7, 9, 3], [5, 3, 8, 6, 9, 7, 1, 2, 4]]
mostevils = [[9, 8, 7, 6, 5, 4, 3, 2, 1], [2, 4, 6, 1, 7, 3, 9, 8, 5], [3, 5, 1, 9, 2, 8, 7, 4, 6], [1, 2, 8, 5, 3, 7, 6, 9, 4], [6, 3, 4, 8, 9, 2, 1, 5, 7], [7, 9, 5, 4, 6, 1, 8, 3, 2], [5, 1, 9, 2, 8, 6, 4, 7, 3], [4, 7, 2, 3, 1, 9, 5, 6, 8], [8, 6, 3, 7, 4, 5, 2, 1, 9]]
twos = [[3, 2, 4, 1], [1, 4, 2, 3], [4, 3, 1, 2], [2, 1, 3, 4]]
easys = [[6, 7, 5, 3, 8, 4, 9, 2, 1], [1, 9, 8, 6, 5, 2, 7, 4, 3], [4, 2, 3, 9, 1, 7, 8, 5, 6], [7, 8, 9, 1, 4, 6, 5, 3, 2], [2, 1, 6, 7, 3, 5, 4, 9, 8], [3, 5, 4, 2, 9, 8, 6, 1, 7], [9, 4, 2, 8, 7, 3, 1, 6, 5], [5, 6, 7, 4, 2, 1, 3, 8, 9], [8, 3, 1, 5, 6, 9, 2, 7, 4]]


def sol(x):
    sol = sudoku(x).solve()['solution']
    return sol

def test_easy():
    assert (sol(easy) == easys)

def test_medium():
    assert (sol(medium) == mediums)

def test_hard():
    assert (sol(hard) == hards)

def test_evil():
    assert (sol(evil) == evils)

def test_mostEvil():
    assert (sol(mostEvil) == mostevils)

def test_two():
    assert (sol(two) == twos)
