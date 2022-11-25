def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def count_fib(func):
    def count(n):
        count.call_count += 1
        return func(n)
    count.call_count = 0
    return count

fib = count_fib(fib)