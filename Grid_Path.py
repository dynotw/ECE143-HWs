# Python 3 program to count number of paths
# in a maze with obstacles.

R = 4
C = 4


# Returns count of possible paths in a
# maze[R][C] from (0,0) to (R-1,C-1)
def countPaths(maze):
    # If the initial cell is blocked,
    # there is no way of moving anywhere
    if (maze[0][0] == -1):
        return 0

    # Initializing the leftmost column
    for i in range(R):
        if (maze[i][0] == 0):
            maze[i][0] = 1

        # If we encounter a blocked cell in
        # leftmost row, there is no way of
        # visiting any cell directly below it.
        else:
            break

    # Similarly initialize the topmost row
    for i in range(1, C, 1):
        if (maze[0][i] == 0):
            maze[0][i] = 1

        # If we encounter a blocked cell in
        # bottommost row, there is no way of
        # visiting any cell directly below it.
        else:
            break

    # The only difference is that if a cell is -1,
    # simply ignore it else recursively compute
    # count value maze[i][j]
    for i in range(1, R, 1):
        for j in range(1, C, 1):

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
    if (maze[R - 1][C - 1] > 0):
        return maze[R - 1][C - 1]
    else:
        return 0


# Driver code
if __name__ == '__main__':
    maze = [[0, 0, 0, ],
            [0, -1, 0, 0],
            [-1, 0, 0, 0],
            [0, 0, 0, 0]]
    print(countPaths(maze))

# This code is contributed by
# Surendra_Gangwar


# if __name__ == '__main__':
#     y=count_paths(3,4,[(0,3),(1,1)])
#     print(y)

maze=np.zeros((m,n))
for i in block:
    maze[i[0],i[1]]=1
