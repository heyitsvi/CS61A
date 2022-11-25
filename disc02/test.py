# def make_keeper(n):
#     """Returns a function which takes one parameter cond and prints
#     out all integers 1..i..n where calling cond(i) returns True.

#     >>> def is_even(x):
#     ...     # Even numbers have remainder 0 when divided by 2.
#     ...     return x % 2 == 0
#     >>> make_keeper(5)(is_even)
#     2
#     4
#     """
#     def check_cond(cond):
#         i=1
#         while (i <= n):
#             if (cond(i) == True):
#                 print(i)
#             i += 1
#     return check_cond

# from numpy import inner


# def make_keeper_redux(n):
#     """Returns a function. This function takes one parameter <cond>
#     and prints out all integers 1..i..n where calling cond(i)
#     returns True. The returned function returns another function
#     with the exact same behavior.

#     >>> def multiple_of_4(x):
#     ...     return x % 4 == 0
#     >>> def ends_with_1(x):
#     ...     return x % 10 == 1
#     >>> k = make_keeper_redux(11)(multiple_of_4)
#     4
#     8
#     >>> k = k(ends_with_1)
#     1
#     11
#     """
#     def check_cond(cond):
#         i=1
#         while (i <= n):
#             if (cond(i) == True):
#                 print(i)
#             i += 1
#         # i=1
#         return make_keeper_redux(n)
#     return check_cond
    

# curry2 = lambda f: lambda x: lambda y: f(x,y)

# print(curry2(add)(3)(2))

# def print_n(n):
#     """
#     >>> f = print_n(2)
#     >>> f = f("hi")
#     hi
#     >>> f = f("hello")
#     hello
#     >>> f = f("bye")
#     done
#     >>> g = print_n(1)
#     >>> g("first")("second")("third")
#     first
#     done
#     done
#     <function inner_print>
#     """
#     def inner_print(x):
#         if n <= 0:
#             print("done")
#         else:
#             print(x)
#         return print_n(n-1)
#     return inner_print

import string


# def remove(n,digit):
#     """
#     >>> remove(231,3)
#     21
#     >>> remove(243132, 2)
#     4313
#     """
#     kept = 0
#     digits = 0
#     while (n != 0):
#         last = n % 10
#         n = n // 10
#         if (last != digit):
#             kept = last
#             digits = int(str(d) 