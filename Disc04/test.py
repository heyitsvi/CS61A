from itertools import count
from operator import index


def count_stair_ways(n):
    """Returns the number of ways to climb up a flight of
    n stairs, moving either 1 step or 2 steps at a time.
    >>> count_stair_ways(4)
    5
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return count_stair_ways(n-1) + count_stair_ways(n - 2)

def count_k(n, k):
    """ Counts the number of paths up a flight of n stairs
    when taking up to and including k steps at a time.
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1
    """

    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        i = 1
        value = 0
        while(i <= k):
            value += count_k(n - i,k)
            i+=1
        return value

# def even_weighted(s):
#     """
#     >>> x = [1, 2, 3, 4, 5, 6]
#     >>> even_weighted(x)
#     [0, 6, 20]
#     """
#     return [(x) * (index(x-1)) for x in s if index(x-1) % 2 == 0]

def my_sum(list):
    def check(value,sum):
        if value < len(list):
            return check(value + 1, sum + list[value])
        return sum

    return check(0, 0)
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
        