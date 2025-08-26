def areaOfMaxDiagonal(self, dimensions: list[list[int]]) -> int:
    def calcDiagonal(a : int, b : int):   
        return a * a + b * b

    def calcSquare(a : int, b : int):
        return a * b

    maximum_diagonal = 0
    max_square = 0
    at_least_two_max_diagonals : bool = False
    
    for dim in dimensions:
        diagonal = calcDiagonal(dim[0], dim[1])
        local_square = calcSquare(dim[0], dim[1]) 

        if(diagonal > maximum_diagonal):
            maximum_diagonal = diagonal
            max_square = local_square
        elif(diagonal == maximum_diagonal):
            at_least_two_max_diagonals = True

            if(local_square > max_square):
                max_square = local_square

    return max_square


#dimensions = [[9,3],[8,6]]
#dimensions = [[4,10],[4,9],[9,3],[10,8]]
#dimensions = [[5,10],[3,7],[8,6],[8,6],[5,9],[10,5],[7,8],[1,9],[2,5],[6,6]]
#dimensions = [[6,2],[8,2],[6,8],[7,6],[1,2],[6,8],[10,9],[2,8]]

print(areaOfMaxDiagonal(None, dimensions))


#
#    Runtime: 0ms; Beats 100.00%
#    Memory: 17.58MB; Beats 98.45%
#
