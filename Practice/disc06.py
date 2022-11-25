def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    count = sum([1 for value in s if value == x])
    for i in range(count):
        s.append(el)

def filter_iter(iterable, fn):
    """
    >>> is_even = lambda x: x % 2 == 0
    >>> list(filter_iter(range(5), is_even)) # a list of the values yielded from the call to filter_iter
    [0, 2, 4]
    >>> all_odd = (2*y-1 for y in range(5))
    >>> list(filter_iter(all_odd, is_even))
    []
    >>> naturals = (n for n in range(1, 100))
    >>> s = filter_iter(naturals, is_even)
    >>> next(s)
    2
    >>> next(s)
    4
    """
    "*** YOUR CODE HERE ***"
    for val in iter(iterable):
        if fn(val) == True:
            yield val

# def merge(a, b):
#     """
#     >>> def sequence(start, step):
#     ...     while True:
#     ...         yield start
#     ...         start += step
#     >>> a = sequence(2, 3) # 2, 5, 8, 11, 14, ...
#     >>> b = sequence(3, 2) # 3, 5, 7, 9, 11, 13, 15, ...
#     >>> result = merge(a, b) # 2, 3, 5, 7, 8, 9, 11, 13, 14, 15
#     >>> [next(result) for _ in range(10)]
#     [2, 3, 5, 7, 8, 9, 11, 13, 14, 15]
#     """
#     "*** YOUR CODE HERE ***"
#     while(True):
#         seq1 = next(a)
#         seq2 = next(b)

#         if seq1 < seq2:
#             yield seq1
#             yield seq2
#         elif seq2 < seq1:
#             yield seq2
#             yield seq1
#         else:
#             yield seq1

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def helper(i):
        if i > (n ** 0.5): # Could replace with i == n
            return True
        elif n % i == 0:
            return False
        return helper(i + 1)
    return helper(2)

def primes_gen(n):
    """Generates primes in decreasing order.
    >>> pg = primes_gen(7)
    >>> list(pg)
    [7, 5, 3, 2]
    """
    if n == 1:
        return [] 
    if is_prime(n) == True:
        yield n
    yield from primes_gen(n-1)