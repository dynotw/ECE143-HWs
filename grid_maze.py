# Some part of the code come from
# https://www.geeksforgeeks.org/count-number-ways-reach-destination-maze/
import numpy as np
def count_paths(m,n,blocks):
    '''

    :param m: input，number of rows
    :param n: input, number of columns
    :param blocks: input, a list showing the positions of obstacle
    :return:
    '''

    assert isinstance(m,int)
    assert m>0
    assert isinstance(n,int)
    assert n>0
    assert isinstance(blocks,list)

    maze = np.zeros((m, n))
    for i in blocks:
        maze[i[0], i[1]] = -1

    # Initializing the leftmost column
    for i in range(m):
        if (maze[i][0] == 0):
            maze[i][0] = 1

        # If we encounter a blocked cell in leftmost row,
        # there is no way of visiting any cell directly below it.
        else:
            break

    # Similarly initialize the topmmost row
    for i in range(1, n):
        if (maze[0][i] == 0):
            maze[0][i] = 1

        # If we encounter a blocked cell in bottommost row,
        # there is no way of visiting any cell directly below it.
        else:
            break

    # The only difference is that if a cell is -1,
    # simply ignore it else recursively compute
    # count value maze[i][j]
    for i in range(1, m):
        for j in range(1, n):

            # If blockage is found, ignore this cell
            if (maze[i][j] == -1):
                continue

            # If we can reach maze[i][j] from
            # maze[i-1][j] then increment count.
            if (maze[i - 1][j] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i - 1][j])

            # If we can reach maze[i][j] from
            # maze[i][j-1] then increment count.
            if (maze[i][j - 1] > 0):
                maze[i][j] = (maze[i][j] +
                              maze[i][j - 1])

            # If the final cell is blocked,
    # output 0, otherwise the answer
    if (maze[m - 1][n - 1] > 0):
        return maze[m - 1][n - 1]
    else:
        return 0

# if __name__ == '__main__':
#     print(count_paths(3,4,[(0,3),(1,1)]))
