import numpy as np
def count_paths(m,n,blocks):
    '''

    :param m:
    :param n:
    :param blocks:
    :return:
    '''

    assert isinstance(m,int)
    assert m>0
    assert isinstance(n,int)
    assert n>0
    assert isinstance(blocks,list)

    start=[0,0]
    while start not in blocks:
        if start[0]+1 <=m-1:
            start[0]+=start[0]+1
        elif start[1]+1 <=n-1:
            start[1]=start[1]+1

def check_route(labyrinth):
    MOVE = {"S": (1, 0), "N": (-1, 0), "W": (0, -1), "E": (0, 1)}
    # copy maze
    route = [row[:] for row in labyrinth]
    pos = (1, 1)
    goal = (10, 10)
    for i, d in enumerate(route):
        move = MOVE.get(d, None)
        if not move:
            print("Wrong symbol in route")
            return False
        pos = pos[0] + move[0], pos[1] + move[1]
        if pos == goal:
            return True
        if labyrinth[pos[0]][pos[1]] == 1:
            print("Player in the pit")
            return False
    print("Player did not reach exit")
    return False

if __name__ == '__main__':
    x=np.array([
[1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,1,0,0,0,1,0,0,1],
[1,0,1,0,0,0,1,0,0,0,1,1],
[1,0,0,0,1,0,0,0,1,0,0,1],
[1,0,1,0,0,0,1,0,0,0,1,1],
[1,0,0,0,1,0,0,0,1,0,0,1],
[1,0,1,0,0,0,1,0,0,0,1,1],
[1,0,0,0,1,0,0,0,1,0,0,1],
[1,0,1,0,0,0,1,0,0,0,1,1],
[1,0,0,0,1,0,0,0,1,0,0,1],
[1,0,1,0,0,0,1,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1],
])
    y=check_route(x)
    print(y)