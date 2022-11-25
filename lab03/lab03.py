from ctypes import sizeof
from operator import add, mul
import re

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1

def has_digit(n, k):
    """Returns whether K is a digit in N.
    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    count = 0
    while (n > 0):
        if (n % 10 == k):
            count += 1
        n = n // 10
    if (count >= 1):
        return True
    return False

def check_in_prev(arr, digit):
    for i in range(0, len(arr)):
        if (arr[i] == digit):
            return True
    return False

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(1313131) # 1 and 3
    2
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(10000) # 0 and 1
    2
    >>> unique_digits(101) # 0 and 1
    2
    >>> unique_digits(10) # 0 and 1
    2
    """
    prev_digits = []
    count = 0
    num = n
    while(n > 0):
        digit = n % 10
        # print("DEBUG: Array", prev_digits)
        if (has_digit(num,digit) == True):
            # print("DEBUG: Check in prev for",digit, check_in_prev(prev_digits, digit))
            if (check_in_prev(prev_digits, digit) == False):
                count += 1
        n = n // 10
        prev_digits.append(digit)
    return count












def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    def num_of_digits(num):
        count = 0
        while(num > 0):
            count += 1
            num = num // 10
        return count
    power = num_of_digits(x)
    while(power > 1):
        first_digit = x % 10
        print("DEBUG: first digit", first_digit)
        second_digit = (x // 10) % 10
        print("DEBUG: second digit", second_digit)
        if (first_digit >= second_digit):
            power -= 1
            x = x // 10
            continue
        else:
            return False
    return True

        


def get_k_run_starter(n, k):
    """
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while i <= k:
        while ((n // 10) % 10) < (n % 10) and n > 10:
            n = n // 10
            # print("DEBUG: N ", n)
        final = n % 10
        i += 1
        n = n // 10
    return final


def make_repeater(func, n):
    """Return the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    def func2(num, n=n):
        while(n > 0):
            num = func(num)
            n -= 1
        return num
    return func2


def composer(func1, func2):
    """Return a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f


def apply_twice(func):
    """ Return a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    return make_repeater(func,2)


def protected_secret(password, secret, num_attempts):
    """
    Returns a function which takes in a password and prints the SECRET if the password entered matches
    the PASSWORD given to protected_secret. Otherwise it prints "INCORRECT PASSWORD". After NUM_ATTEMPTS
    incorrect passwords are entered, the secret is locked and the function should print "SECRET LOCKED".

    >>> my_secret = protected_secret("correcthorsebatterystaple", "I love UCB", 2)
    >>> my_secret = my_secret("hax0r_1") # 2 attempts left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("correcthorsebatterystaple")
    I love UCB
    >>> my_secret = my_secret("hax0r_2") # 1 attempt left
    INCORRECT PASSWORD
    >>> my_secret = my_secret("hax0r_3") # No attempts left
    SECRET LOCKED
    >>> my_secret = my_secret("correcthorsebatterystaple")
    SECRET LOCKED
    """

    def get_secret(password_attempt):
        print("DEBUG 1:", password, secret, num_attempts)
        # print("DEBUG 3:",(password_attempt == password))
        if(password_attempt == password and num_attempts > 0):
            # print("DEBUG 4:", password, secret, num_attempts)
            print(secret)
            return protected_secret(password,secret,num_attempts)
        elif(password != password_attempt and num_attempts > 0):
            print("INCORRECT PASSWORD")
            # print("DEBUG 2:", password, secret, num_attempts)
            return protected_secret(password,secret,(num_attempts - 1))
        else:
            print("SECRET LOCKED")
            return protected_secret(password,secret,0)
            # print("DEBUG: ",password,secret,num_attempts)
            # num_attempts = num_attempts - 1
            # num_attempts -= 1

    return get_secret

def typewriter(word):
    """A function that keeps track of a word as it's being typed."
    >>> t = typewriter("he")
    he
    >>> t = t("llo")
    hello
    >>> t = t(" w")
    hello w
    >>> t = t("orld!")
    hello world!
    """
    def typing(next_str):
        # print(word + next_str)
        return typewriter(word + next_str)
    print(word)
    return typing

def composer(func=lambda x: x):
    """
    Returns two functions -
    one holding the composed function so far, and another
    that can create further composed problems.
    >>> add_one = lambda x: x + 1
    >>> mul_two = lambda x: x * 2
    >>> f, func_adder = composer()
    >>> f1, func_adder = func_adder(add_one)
    >>> f1(3)
    4
    >>> f2, func_adder = func_adder(mul_two)
    >>> f2(3) # should be 1 + (2*3) = 7
    7
    >>> f3, func_adder = func_adder(add_one)
    >>> f3(3) # should be 1 + (2 * (3 + 1)) = 9
    9
    """
    def func_adder(g):
        return composer(lambda x: func(g(x)))
    return func, func_adder

def both_paths(sofar="S"):
    """
    >>> up, down = both_paths()
    S
    >>> upup, updown = up()
    SU
    >>> downup, downdown = down()
    SD
    >>> _ = upup()
    SUU
    """
    
    def up():
        return both_paths(sofar + "U")

    def down():
        return both_paths(sofar + "D")
    print(sofar)
    return up, down

def is_even(x):
    if x % 2 == 0:
        print('even')
    print('odd')
    return x - 1

def is_ascending(n):
    """Returns True if the digits of N are in ascending order.

    >>> is_ascending(321)
    True
    >>> is_ascending(123)
    False
    >>> is_ascending(4432221)
    True
    >>> is_ascending(5492)
    False
    >>> is_ascending(5420)
    True
    """
    while(n > 10):
        if (((n // 10) % 10) >= (n % 10)):
            n = n // 10
        else:
            return False
    
    return True


def count_one(n):
    """Counts the number of 1s in the digits of n
    >>> count_one(7007)
    0
    >>> count_one(123)
    1
    >>> count_one(161)
    2
    >>> count_one(1)
    1
    """
    count = 0
    while(n > 0):
        if(n % 10 == 1):
            count += 1
        n = n // 10

    return count

def total_ones(n):
    """Returns number of 1s in the digits of all numbers from 1 to
    n.

    >>> total_ones(10) # 1, 10 -> two 1s
    2
    >>> total_ones(15) # 1, 10, 11, 12, 13, 14, 15 -> eight 1s
    8
    >>> total_ones(21)
    13
    """
    count = 0
    while(n > 0):
        count += count_one(n)
        n -= 1

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
            number = number // 10
            n += 1
        return new_number

    return check

def run_checker(condition, result):
    """
    Returns a chain function. Each call in a chain that starts with
    this returned function prints "No run!" if CONDITION returns a false
    value when applied to the previous two arguments and the current argument,
    and otherwise prints the result of applying RESULT to these same
    three arguments. For calls in the chain where there are fewer than two
    preceding calls in the chain, the missing arguments are taken to be -1.
    >>> f = run_checker(lambda a, b, c: a > b > c and a >= 10, lambda a, b, c: a*(b+c))
    >>> f = f(15)
    No run!
    >>> f = f(10)
    No run!
    >>> f = f(5)
    225
    >>> f = f(2)
    70
    >>> f = f(1)
    No run!
    >>> f = f(11)
    No run!
    >>> f = f(12)
    No run!
    >>> f = f(10)
    No run!
    >>> f = f(2)
    144
    """
    def f(a,b):
    # (a)
        def g(c):
            # (b)
            if (condition(a,b,c) == True):
                print(result(a,b,c))
            else:
                print("No run!")
            return f(a=b,b=c)
            # (c)
        return g
    return f(a=-1,b=-1)


# def count(element, box):
#     """Count how many times digit element appears in integer box.
#     >>> count(2, 222122)
#     5
#     >>> count(0, -2020)
#     2
#     >>> count(0, 0) # 0 has no digits
#     0
#     """
#     assert element >= 0 and element < 10
#     _________
#     total = 0
#     while box > 0:
#         if box % 10 == element:
#             total = _________
#         box = box // 10
#     return total
def next_hail(k):
    """Return the next element in a hailstone sequence."""
    assert k > 1
    if k % 2 == 0:
        return k // 2
    else:
        return 3 * k + 1

# Luhn Sum : https://pythontutor.com/visualize.html#code=def%20split%28n%29%3A%0A%20%20%20%20return%20n%20//%2010,%20n%20%25%2010%0A%0Adef%20sum_digits%28n%29%3A%0A%20%20%20%20if%20n%20%3C%2010%3A%0A%20%20%20%20%20%20%20%20return%20n%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20all_but_last,%20last%20%3D%20split%28n%29%0A%20%20%20%20%20%20%20%20return%20sum_digits%28all_but_last%29%20%2B%20last%0Adef%20luhn_sum%28n%29%3A%0A%20%20%20%20if%20n%20%3C%2010%3A%0A%20%20%20%20%20%20%20%20return%20n%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20all_but_last,%20last%20%3D%20split%28n%29%0A%20%20%20%20%20%20%20%20return%20luhn_sum_double%28all_but_last%29%20%2B%20last%0Adef%20luhn_sum_double%28n%29%3A%0A%20%20%20%20all_but_last,%20last%20%3D%20split%28n%29%0A%20%20%20%20luhn_digit%20%3D%20sum_digits%282*last%29%0A%20%20%20%20if%20n%20%3C%2010%3A%0A%20%20%20%20%20%20%20%20return%20luhn_digit%0A%20%20%20%20else%3A%20%0A%20%20%20%20%20%20%20%20return%20luhn_sum%28all_but_last%29%20%2B%20luhn_digit%0Aluhn_sum%287242%29&cumulative=false&curInstr=55&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false

def multiply(m,n):
    if(n == 1):
        return m 
    else:
        return m + multiply(m,n-1) 

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    if n == 1:
        return 1
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def check(index):
        if (n % index == 0 and index < n):
            return False
        elif(n % index != 0 and index < n):
            return check(index + 1)
        return True
    return check(2)

def recursive_hailstone(n):
    print(n)
    if n == 1:
        return 1
    else:
        if(n % 2 == 0):
            return recursive_hailstone(n // 2)
        else:
            return recursive_hailstone((n * 3) +1)

# def merge(n1, n2):
#     """ Merges two numbers by digit in decreasing order
#     >>> merge(31, 42)
#     4321
#     >>> merge(21, 0)
#     21
#     >>> merge (21, 31) 
#     3211
#     """
#     if (n1 == 0):
#         return n2
#     if (n2 == 0):
#         return n1
#     def smallest_digit(n1,n2):
#         smallest =  min((n1 % 10),(n1 // 10), (n2 % 10),(n2 // 10)) 
#         if(smallest_digit == n2 % 10 or smallest_digit == n2 // 10):
#             if(smallest_digit = n2 % 10):
#                 return 

#     return smallest_digit(n1,n2)