# Prob_link: https://www.codingninjas.com/studio/problems/valid-sudoku_8230704?challengeSlug=striver-sde-challenge&leftPanelTab=0

def isItSudoku(matrix):
    for i in range(9):

        for j in range(9):

            if matrix[i][j] == 0:

                for k in range(1, 10):

                    if valid(i, j, k, matrix):

                        matrix[i][j] = k

                        if isItSudoku(matrix):

                            return True

                        else:

                            matrix[i][j] = 0

                return False

    return True


def valid(i, j, k, matrix):
    for l in range(9):

        if matrix[l][j] == k:
            return False

        if matrix[i][l] == k:
            return False

        if matrix[3 * (i // 3) + l // 3][3 * (j // 3) + l % 3] == k:
            return False

    return True