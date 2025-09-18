def lenOfVDiagonal(self, grid: list[list[int]]) -> int:
    def max_in_list(array):
        max_val = 0
        for el in array:
            if(el > max_val):
                max_val = el

        return max_val

    def DFSinGrid(grid, x : int, y : int):
        segments = { } # keys = (coordinates), values = [sequenceses]

        


        return max_in_list(size_of_segments)
    
    n = len(grid)
    m = len(grid[0]) # because matrix

    global_max_segm = 0
    
    for idx_n in range(n):
        for idx_m in range(m):
            if(grid[idx_n][idx_m] == 1):
                curr_max_segm = DFSinGrid(grid, idx_n, idx_m)
                if(curr_max_segm > global_max_segm):
                    global_max_segm = curr_max_segm
                 
    return global_max_segm
    

grid = [[2,2,1,2,2],[2,0,2,2,0],[2,0,1,1,0],[1,0,2,2,2],[2,0,0,2,2]]
print(lenOfVDiagonal(None, grid))


# You are given a 2D integer matrix grid of size n x m, where each element is either 0, 1, or 2.

# A V-shaped diagonal segment is defined as:

# The segment starts with 1.
# The subsequent elements follow this infinite sequence: 2, 0, 2, 0, ....
# The segment:
# Starts along a diagonal direction (top-left to bottom-right, bottom-right to top-left, top-right to bottom-left, or bottom-left to top-right).
# Continues the sequence in the same diagonal direction.
# Makes at most one clockwise 90-degree turn to another diagonal direction while maintaining the sequence.

# Return the length of the longest V-shaped diagonal segment. If no valid segment exists, return 0.