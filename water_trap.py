# This code is modified from
# https://www.geeksforgeeks.org/trapping-rain-water/
def get_trapped_water(seq):
    '''

    :param seq: input, list
    :return: int
    '''

    assert isinstance(seq,list)

    n=len(seq)
    # left[i] contains height of tallest bar to the left of i th bar including itself
    left_bar = [0] * n

    # Right [i] contains height of tallest bar to the right of i th bar including itself
    right_bar = [0] * n

    # Initialize result
    trap_water = 0

    # Fill left array, because there is no left column for 0th bar, 0th bar = itself(seq[0])
    left_bar[0] = seq[0]
    for i in range(1, n):
        left_bar[i] = max(left_bar[i - 1], seq[i])

    # Fill right array, n th bar =itself(seq[-1]), because there is no right column for n th bar
    # Just the inverse operation like the above one (left array)
    right_bar[-1] = seq[-1]
    for i in range(n-2, -1, -1):
        right_bar[i] = max(right_bar[i + 1], seq[i])

    # Calculate the accumulated water element by element
    # Just put the left[i], right[i] and seq[i], together
    # consider the amount of water on i th bar, the amount of water accumulated on this particular.

    # we only need to calculate 2nd to last 2nd column
    for i in range(1, n):
        trap_water += min(left_bar[i], right_bar[i]) - seq[i]

    return trap_water
#
# if __name__ == '__main__':
#     print(get_trapped_water([3, 0, 1, 3, 0, 5]))


