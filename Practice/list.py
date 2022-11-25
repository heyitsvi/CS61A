#Creating a list

def tree(label, branches = []):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) !=  list or len(tree) < 1:
        return False
    else:
        for branch in branches(tree):
            if not is_tree(branch):
                return False
    return True

def is_leaf(tree):
    return (branches(tree) == [])

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        fib_n = label(left) + label(right)
        return tree(fib_n, [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    else:
        total = [count_leaves(b) for b in branches(t)]
        return sum(total)

def double_tree(t):
    if is_leaf(t):
        return tree(label(t) * 2)
    else:
        return tree(label(t) * 2, [double_tree(b) for b in branches(t)])

def list_of_leaves(t):
    if is_leaf(t):
        return [label(t)]
    else:
        leaves = [list_of_leaves(b) for b in branches(t)]
        return sum(leaves, [])




















# def count_leaves(tree):
#     if is_leaf(tree):
#         return 1
#     else:
#         branch_counts = [count_leaves(b) for b in branches(tree)]
#         return sum(branch_counts)

# def double(t):
#     if is_leaf(t):
#         return tree(label(t) * 2)
#     else:
#         return tree(label(t) * 2, [double(b) for b in branches(t)])
# def tree(root_label, branches=[]):
#     for branch in branches:
#         assert is_tree(branch), 'branches must be trees'
#     return [root_label] + list(branches)
# def label(tree):
#     return tree[0]
# def branches(tree):
#     return tree[1:]
# def is_leaf(tree):
#     return len(branches(tree)) == 0

# def count_leaves(tree):
#     if 


# def print_tree(t, indent = 0):
#     print(indent * " " + str(label(t)))
#     [print_tree(b, indent + 2) for b in branches(t)]

# def count_paths(t, total):
#     if label(t) == total:
#         return 1
    


