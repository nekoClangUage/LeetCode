def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
    if(mat == [[]]):
        return [[]]

    direct_upward : bool = True
    output_list = []
    count_elements = 0

    for i in range(0, len(mat)):
        for j in mat[i]:
            count_elements += 1

    i = 0 
    j = 0
    m = len(mat)
    n = len(mat[0])

    end_point = (len(mat) - 1, len(mat[len(mat) - 1]) - 1)

    while((i, j) != end_point):
        # 01 
        # 10

        i_lim_0 = i < m
        i_lim_1 = i >= 0

        j_lim_0 = j < n
        j_lim_1 = j >= 0

        i_limit = (i_lim_0 and i_lim_1)
        j_limit = (j_lim_0 and j_lim_1)

        if( i_limit and j_limit ):
            output_list.append(mat[i][j])
            n = len(mat[i])
            if(direct_upward):
                i -= 1
                j += 1
            else:
                i += 1
                j -= 1
        elif(not i_lim_0 and not j_lim_1):
            i += (-1)
            j += (2)
            direct_upward = not(direct_upward)
        elif(not j_lim_0 and not i_lim_1):
            i += (2)
            j += (-1)
            direct_upward = not(direct_upward)
        elif(not j_lim_1):
            j += ( 1)
            direct_upward = not(direct_upward)
        elif(not i_lim_1):
            i += ( 1)
            direct_upward = not(direct_upward)
        elif(not i_lim_0 and j_lim_1):
            i += (-1)
            j += (2)
            direct_upward = not(direct_upward)
        elif(not j_lim_0 and i_lim_1):
            i += (2)
            j += (-1)
            direct_upward = not(direct_upward)
    
    output_list.append(mat[i][j])

    return output_list


# different test-cases
#mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#mat = [[1,2,3,4],[5,6,7,8]]
#mat = [[7],[9],[6]]
#mat = [[1,2,3,4],[5,6,7,8]]
#mat = [[2, 3]]

print(findDiagonalOrder(None, mat))

#
#    Runtime: 2ms; Beats 67.00%
#    Memory: 19.73MB; Beats 59.95%
#
