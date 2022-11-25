from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> # a check that you didn't change the return statement!
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(x, y, z):
    """Return a*a + b*b, where a and b are the two smallest members of the
    positive numbers x, y, and z.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    >>> # check that your code consists of nothing but an expression (this docstring)
    >>> # a return statement
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    return x*x + y*y + z*z - (max(x,y,z))**2


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"

    num = 1
    for i in range (2, n):
        if (n % i == 0):
            num = i
        else:
            continue
    return num


def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result


def with_if_statement():
    """
    >>> result = with_if_statement()
    47
    >>> print(result)
    None
    """
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    """
    >>> result = with_if_function()
    42
    47
    >>> print(result)
    None
    """
    return if_function(cond(), true_func(),false_func())

def cond():
    "*** YOUR CODE HERE ***"
    return (False)

def true_func():
    "*** YOUR CODE HERE ***"
    # print(42)
    print(42)

def false_func():
    "*** YOUR CODE HERE ***"
    print(47)


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    while (n != 1): 
        print(n)
        if (n % 2 == 0):
            n = int (n/2)
        else:
            n = int (n * 3 + 1)
        count=count + 1
    print(1)
    return count
    
def digit_replacer(predicate, transformer):
    """Returns a function that accepts a single number N (where N > 0) and
    returns a number where all digits that return true for PREDICATE(DIGIT)
    have been replaced by TRANSFORMER(DIGIT). TRANSFORMER is assumed to always
    return a valid digit >= 0 and <= 9.
    >>> is_even = lambda d: d % 2 == 0
    >>> lt_five = lambda d: d < 5
    >>> always_two = lambda d: 2
    >>> floor_divide_two = lambda d: d // 2
    >>> digit_replacer(is_even, floor_divide_two)(21098)
    11094
    >>> digit_replacer(lt_five, always_two)(1064592)
    2262592
    """
    def check(number):
        new_number = 0
        n = 0
        while(number > 0):
            last_digit = number % 10
            if(predicate(last_digit) == True):
                last_digit = transformer(last_digit)
            new_number += last_digit*(10 ** (n))
            n = n // 10
        return new_number

    return check
        

