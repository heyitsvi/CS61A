
def getIndices(lst):
    lst = list(map(lambda x: abs(x), lst))
    min_value = min(lst)
    result = []
    for i in range(len(lst)):
        if lst[i] == min_value:
            result.append(i)
    return result

def max_adjacent_sum(lst):
    max_sum = 0
    for i in range(len(lst) - 1):
        if (lst[i] + lst[i+1]) > max_sum:
            max_sum = lst[i] + lst[i+1]

    return max_sum

def create_dictionary(lst):
    last_digits = [x % 10 for x in lst]
    return {d: [x for x in lst if x % 10 == d] for d in range(0,10) if d in last_digits}
