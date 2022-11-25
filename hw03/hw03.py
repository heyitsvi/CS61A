# from numpy import array, character


# from numpy import diff


HW_SOURCE_FILE = __file__


def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    def check(count,pos):
        if(pos % 10 == 8):
            return check(count + 1,pos // 10)
        if(pos <= 0):
            return count
        return check(count, pos // 10)
    return check(0,pos)

def check_for_digit(pos, digit):
    arr = list(str(pos))
    count = 0
    for item in arr:
        if(item  == str(digit)):
            count += 1
    return count

def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    def keep_count(sum_count, count, sign):
        if(count == n):
            return sum_count
        if(count % 8 == 0 or num_eights(count) >= 1):
            if (sign == "add"):
                return keep_count(sum_count - 1, count + 1, "sub")
            else:
                return keep_count(sum_count + 1, count + 1, "add")
        if(sign == "add"):
            return keep_count(sum_count + 1, count + 1, "add")
        if(sign == "sub"):
            return keep_count(sum_count - 1, count + 1, "sub")
    return keep_count(1,1,"add")
    


def missing_digits(n):
    """Given a number a that is in sorted, non-decreasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.
    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    >>> from construct_check import check
    >>> # ban while or for loops
    >>> check(HW_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    def check(count,n):
        last_digit = n % 10
        # print("DEBUG: Last Digit = ", last_digit)
        second_last_digit = (n // 10) % 10
        # print("DEBUG: Second Last Digit = ", second_last_digit)
        if n < 10: 
            return count
        if (last_digit == second_last_digit): 
            return check(count, n // 10)
        if(second_last_digit < (last_digit)):
            difference = last_digit - second_last_digit - 1
            return check(count + difference, n // 10) 
    return check(0,n)
    # def check(count,n, num):
    #     print("DEBUG: N = ", n)
    #     if n == 0:
    #         return count
    #     if n > 0 and n < 10:
    #         return n
    #     if ((n // 10) % 10 == n % 10):
    #         return check(count, n // 10, (n // 10) % 10)
    #     if (check_for_digit(n, num - 1) == 0 and (num - 1) > ((n // 10) % 10)):
    #         print("DEBUG: num = ", num)
    #         print("DEBUG: count = ", count)
    #         return check(count + 1, n, num - 1)
    #     else:
    #         return check(count, n // 10, (n // 10) % 10)
    # return check(0,n, n % 10)


def ascending_coin(coin):
    """Returns the next ascending coin in order.
    >>> ascending_coin(1)
    5
    >>> ascending_coin(5)
    10
    >>> ascending_coin(10)
    25
    >>> ascending_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def descending_coin(coin):
    """Returns the next descending coin in order.
    >>> descending_coin(25)
    10
    >>> descending_coin(10)
    5
    >>> descending_coin(5)
    1
    >>> descending_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1


def count_coins(change):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    def check(change, biggest_coin):
        # print("DEBUG", change,biggest_coin)
        if change == 0:
            return 1
        elif change < 0:
            return 0
        elif(biggest_coin == 1):
            return 1
        else:
            return check(change - biggest_coin, biggest_coin) + check(change, descending_coin(biggest_coin))

    return check(change, 25)

# https://pythontutor.com/visualize.html#code=def%20descending_coin%28coin%29%3A%0A%20%20%20%20if%20coin%20%3D%3D%2025%3A%0A%20%20%20%20%20%20%20%20return%2010%0A%20%20%20%20elif%20coin%20%3D%3D%2010%3A%0A%20%20%20%20%20%20%20%20return%205%0A%20%20%20%20elif%20coin%20%3D%3D%205%3A%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20%20%20%20%20%0Adef%20count_coins%28change%29%3A%0A%20%20%20%20def%20check%28change,%20biggest_coin%29%3A%0A%20%20%20%20%20%20%20%20if%20change%20%3D%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20%20%20%20%20elif%20biggest_coin%20%3C%3D%200%20or%20change%20%3C%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%200%0A%20%20%20%20%20%20%20%20elif%28biggest_coin%20%3D%3D%201%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20return%20check%28change%20-%20biggest_coin,%20biggest_coin%29%20%2B%20check%28change,%20descending_coin%28biggest_coin%29%29%0A%0A%20%20%20%20return%20check%28change,%2025%29%0Acount_coins%2810%29&cumulative=false&curInstr=77&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)


def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul


def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'
