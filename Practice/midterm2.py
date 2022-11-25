

# class C:
#     x = 'e'
#     def f(self, y):
#         print(repr(self))
#         self.x = self.x + y
#         return self
#     def __str__(self):
#         return 'go'
# class Big(C):
#     x = 'u'
#     def f(self, y):
#         print("C.x", C.x)
#         C.x = C.x + y
#         print(self)
#         return C.f(self, 'm')
#     def __repr__(self):
#         return '<bears>'
# # m = C().f('i')
# # n = Big().f('o')

class Tree:
    def __init__(self ,label ,branches = []):
        self.label = label
        for b in branches:
            assert isinstance(b, Tree)
        self.branches = branches

    def is_leaf(self):
        return self.branches == []

    def __repr__(self):
        if self.branches == []:
            return f'<{self.label}>'
        else:
            rest = ""
            for b in self.branches:
                rest += repr(b)
            return f"<{self.label} " + rest + ">"

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    
    def __getitem__(self,i):
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]
    
    def __len__(self):
        return 1 + len(self.rest)

    def __repr__(self):
        if self.rest is Link.empty:
            return f'Link({self.first})'
        else:
            return "Link(" + f'{self.first}' + ', ' + repr(self.rest) + ")"

def link_expression(s):
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' +  link_expression(s.rest)
    return f'Link({s.first}{rest})'

Link.__repr__ = link_expression

# def max_tree(t, key):
#     return max([t.label] + [max_tree(b,key) for b in t.branches], key=key)

# # def filter_index(f, s):
# #     """Return a Link containing the elements of Link s that have an index i for
# #     which f(i) is a true value.
# #     >>> powers = Link(1, Link(2, Link(4, Link(8, Link(16, Link(32))))))
# #     >>> filter_index(lambda x: x < 4, powers)
# #     Link(1, Link(2, Link(4, Link(8))))
# #     >>> filter_index(lambda x: x % 2 == 1, powers)
# #     Link(2, Link(8, Link(32)))
# #     """
# #     def helper(i, s):
# #         if s is Link.empty:
# #             return s
# #         filtered_rest = helper(i+1,s.rest)
# #         if f(i):
# #             return Link(s.first, filtered_rest)
# #         else:
# #             return filtered_rest
# #     return helper(0,s)

# # def same_shape(t1,t2):
# #     if len(t1.branches) == len(t2.branches):
# #         for b1 in t1.branches:
# #             for b2 in t2.branches:
# #                 same_shape(b1, b2)
# #         return True
# #     else:
# #         return False

# def insert(lst, item, index):
#     if lst.rest is Link.empty:
#         return "Out of Bounds"
#     elif index != 0:
#         return insert(lst.rest, item,index - 1)
#     else:
#         original_value = lst.first
#         lst.first = item
#         lst.rest = Link(original_value, lst.rest)

# def contains(t,e):
#     if t.label == e:
#         return True
#     else:
#         check = [contains(b,e) for b in t.branches]

#     return any(check)

# def all_paths(t):
#     if t.is_leaf():
#         return [[t.label]]
#     else:
#         total = []
#         for b in t.branches:
#             for path in all_paths(b):
#                 print(path)
#                 total.append([t.label] + path)
#         return total

# def max_tree(t):
#     if t.is_leaf():
#         return Tree(t.label)
#     else:
#         branches = [max_tree(b) for b in t.branches]
#         print(branches)
#         root = max([t.label] + [b.label for b in branches])
#         # print(root)
#         return Tree(root, branches)

# # def find_paths(t):
# #     if t.is_leaf():
# #         return [[t.label]]
# #     else:
# #         paths = []
# #         for b in t.branches:
# #             for path in find_paths(b):
# #                 paths.append([t.label] + path)
# #         return paths

# def mapp(fn, lst):
#     if lst is Link.empty:
#         return lst
#     else:
#         lst.first = fn(lst.first)
#         return mapp(fn, lst.rest) 

# def alternate(lst):
#     def helper(index,lst):
#         if lst is Link.empty:
#             return lst
#         else:
#             if index % 2 == 0:
#                 return Link(lst.first, helper(index+1,lst.rest))
#             else:
#                 return helper(index+1, lst.rest)
#     return helper(0, lst)

# def filter_link(fn, lst):
#     if lst is Link.empty:
#         return lst
#     else:
#         if fn(lst.first):
#             return Link(lst.first, filter_link(fn, lst.rest))
#         else:
#             return filter_link(fn, lst.rest)

# def equal(t1,t2):
#     """Returns Tree if t1 and t2 are equal trees.
#     >>> t1 = Tree(1,
#     ...           [Tree(2, [Tree(4)]),
#     ...            Tree(3)])
#     >>> t2 = Tree(1,
#     ...           [Tree(2, [Tree(4)]),
#     ...            Tree(3)])
#     >>> equal(t1, t2)
#     True
#     >>> t3 = Tree(1,
#     ...           [Tree(2),
#     ...            Tree(3, [Tree(4)])])
#     >>> equal(t1, t3)
#     False
#     """
#     if t1.label != t2.label:
#         return False
#     elif len(t1.branches) != len(t2.branches):
#         return False
#     else:
#         return all(equal(child1, child2) for child1, child2 in zip(t1.branches, t2.branches))

# def size(t):
#     return 1 + sum([size(b) for b in t.branches])

# def height(t):
#     if t.is_leaf():
#         return 0
#     else:
#         return 1 + max([height(b) for b in t.branches])

# def same_shape(t1,t2):
#     if len(t1.branches) != len(t2.branches):
#         return False
#     else:
#         return all(same_shape(b1,b2) for b1,b2 in zip(t1.branches, t2.branches))

# def sprout_leaves(t, vals):
#     if t.is_leaf():
#         for val in vals:
#             t.branches += [Tree(val)]
#     else:
#         for b in t.branches:
#             return sprout_leaves(b, vals)

# # def prune_leaves(t, vals):
# #     if t.is_leaf():
# #         if t.label in vals:
# #             return None
# #         else:
# #             return t
# #     new_branches = [prune_leaves(b, vals) for b in t.branches]
# #     t.branches = [b for b in new_branches if b is not None]
# #     return t

# def prune_tree(t, lst):
#     if t.is_leaf():
#         if t.label in lst:
#             return None
#         else:
#             return t    
#     new_branches = [prune_tree(b) for b in t.branches]
#     t.branches = [b for b in new_branches if b is not None]
#     return t

# def get_all_paths(t):
#     if t.is_leaf():
#         return [[t.label]]
#     else:
#         all_paths = []
#         for b in t.branches:
#             for path in get_all_paths(b):
#                 all_paths.append([t.label] + path)
#         return all_paths

# def bst_contains(t, item):
#     if t.label == item:
#         return True
#     else:
#         for b in t.branches:
#             if bst_contains(b,item):
#                 return True
#     return False

# def validate(lst):
#     if lst.rest is Link.empty:
#         return True
#     else:
#         while(lst.rest is not Link.empty):
#             if isinstance(lst.rest, Link):
#                 lst = lst.rest
#             else:
#                 return False
#         return True

# def count_link(r, value):
#     count = 0
#     while(r is not Link.empty):
#         if r.first == value:
#             count+=1
#         r = r.rest
#     return count

# def extend_link(s1,s2):
#     # if s1.rest is Link.empty:
#     #     while s2 is not Link.empty:
#     #         s1.rest = Link(s2.first)
#     #         s1 = s1.rest
#     #         s2 = s2.rest
#     # else:
#     #     return extend_link(s1.rest,s2)
#     if s2 is Link.empty:
#         return 
#     elif s1.rest is Link.empty:
#         s1.rest = Link(s2.first)
#         return extend_link(s1.rest, s2.rest)
#     else:
#         return extend_link(s1.rest, s2)

# def deep_map(fn, lst):
#     if lst is Link.empty:
#         return
#     else:
#         if isinstance(lst.first, Link):
#             deep_map(fn, lst.first)
#         else:
#             lst.first = fn(lst.first)
#         deep_map(fn, lst.rest)

# # class Fibonacci:
# #     def __init__(self):
# #         self.prev = 0
# #         self.next = 1
    
# #     def __iter__(self):
# #         while True:
# #             yield self.next
# #             num = self.prev + self.next
# #             self.prev = self.next
# #             self.next = num 

# def map_gen(fn, iter1):
#     yield from map(fn, iter1)

# def zip_iters(iter1, iter2):
#     try:
#         yield (next(iter1), next(iter2))
#     except:
#         raise StopIteration

# def pascals():
#     """Doctests

#     >>> p = pascals()
#     >>> next(p)
#     [1]
#     >>> next(p)
#     [1, 1]
#     >>> next(p)
#     [1, 2, 1]
#     >>> next(p)
#     [1, 3, 3, 1]
#     >>> next(p)
#     [1, 4, 6, 4, 1]
#     """
#     curr = [1]
#     while True:
#         yield curr
#         i, new = 1, [1]
#         while i < len(curr):
#             new.append(curr[i-1] + curr[i])
#             i += 1
#         new.append(1)
#         curr = new

# #OOP
# class Pokemon:
#     def __init__(self, owner):
#         self.owner = owner
#         self.hp = 10

#     def attack(self, other):
#         if self.hp <= 0:
#             print(self.name + 'is too tired.')
#         else:
#             print('{} used {}!'.format(self.name, self.attack_name))
#             other.hp -= self.damage

# class Pikachu(Pokemon):
#     name = 'Pikachu'
#     damage = 5
#     attack_name = 'thunder'

# class Squirtle(Pokemon):
#     name = 'Squirtle'
#     damage = 3
#     attack_name = 'water gun'

# class Account:
#     """A class computer account. Each account has a two-letter ID
#     and the name of the student who is registered to the account.
#     """
#     num_of_accounts = 0
#     def __init__(self, id):
#         self.id = id
#         Account.num_of_accounts += 1

#     def register(self, student):
#         self.student = student
#         print('Registered!')

#     @property
#     def type(self):
#         return type(self)

# class CircularBuffer:
#     """Doctests:

#     >>> buffer = CircularBuffer(3)
#     >>> buffer.remove()
#     Buffer is empty
#     >>> buffer.append('a')
#     >>> buffer.remove()
#     'a'
#     >>> buffer.remove()
#     Buffer is empty
#     >>> buffer.append('b')
#     >>> buffer.append('c')
#     >>> buffer.append('d')
#     >>> buffer.append('e')
#     Buffer capacity exceeded
#     >>> buffer.remove()
#     'b'
#     >>> buffer.remove()
#     'c'
#     >>> buffer.remove()
#     'd'
#     >>> buffer.remove()
#     Buffer is empty
#     """
#     def __init__(self, n):
#         self.array = [None]*n   # list of length n
#         self.n = n
#         self.start = 0
#         self.end = 0

#     def append(self, elem):
#         if self.end - self.start != self.n:
#             self.array[(self.end % self.n)] = elem
#             self.end += 1
#         else:
#             print("Buffer capacity exceeded")

#     def remove(self):
#         if self.start == self.end:
#             print("Buffer is empty")
#         else:
#             removed_element = self.array[self.start % self.n]
#             self.start += 1
#             return removed_element

# class Chef:
#     """Doctests:

#     >>> albert = Chef('quiche', ['egg', 'cheese', 'cream', 'salt'])
#     >>> ramsay = Chef('steak', ['meat', 'bbq sauce', 'salt'])
#     >>> ramsay.cook()
#     'Not enough ingredients!'
#     >>> ramsay.serve()
#     'No food to serve!'
#     >>> ramsay.fetch_ingredients()     # 1 salt remaining
#     "Fetched: ['meat', 'bbq sauce', 'salt']"
#     >>> ramsay.cook()
#     'Cooked steak!'
#     >>> ramsay.serve()
#     >>> Chef.finished
#     ['steak']
#     >>> albert.fetch_ingredients()     # 0 salt remaining
#     "Fetched: ['egg', 'cheese', 'cream', 'salt']"
#     >>> albert.cook()
#     'Cooked quiche!'
#     >>> albert.serve()
#     >>> Chef.finished
#     ['steak', 'quiche']
#     >>> ramsay.fetch_ingredients()
#     'No more salt!'
#     """
#     finished = []
#     storage = {}

#     def __init__(self, dish, ingredients_lst):
#         self.dish = dish
#         self.ingredients = ingredients_lst
#         for i in ingredients_lst:
#             if i in Chef.storage:
#                 Chef.storage+=1
#     @classmethod
#     def add_ingredients(self, lst):
#         for i in lst:
#             if i in self.storage:
#                 self.storage[i] += 1
#             else:
#                 self.storage[i] = 2

#     def remove_ingredients(self, lst):
#         for i in lst:
#             if i in self.storage:
#                 self.storage[i] += 1

        
# def one_to_one(d):
#     seen_elements = []
#     for elem in d.values():
#         if elem in seen_elements:
#             return False
#         else:
#             seen_elements.append(elem)
#     return True

# def degrees(users, start, end, visited):
#     """Finds the degree of separation between START and END. If
#     START and END are not connected, return infinity: float('inf').

#     PARAMETERS:
#     users   -- dictionary; keys are users, values are friends lists
#     start   -- starting user
#     end     -- ending user
#     visited -- a Python set of users we've already checked
#     """
#     if start == end:
#         return 0
#     smallest = float('inf')     # infinity
#     visited.add(start)
#     for k, v in start.items():
#         if ______:
#             friend_degree = degrees(______)
#             smallest = _______
#     return smallest

# def word_finder(letter_tree, words_list):
#     def helper(word, t):
#         if word in words_list:
#             yield word
#         for b in t.branches:
#             yield from helper(word + b.label, b)
#     yield from helper(letter_tree.label, letter_tree)

# def family(t):
#     result = [t.label]
#     for b in t.branches:
#         result += family(b)
#     return result

# def apply_tree(fn_tree, val_tree):
#     """ Mutates val_tree by applying each function stored in fn_tree
#     to the corresponding labels in val_tree
#     >>> double = lambda x: x*2
#     >>> square = lambda x: x**2
#     >>> identity = lambda x: x
#     >>> t1 = Tree(double, [Tree(square), Tree(identity)])
#     >>> t2 = Tree(6, [Tree(2), Tree(10)])
#     >>> apply_tree(t1, t2)
#     >>> t2
#     Tree(12, [Tree(4), Tree(10)])
#     """
#     val_tree.label = fn_tree.label(val_tree.label)
#     for pair in zip(fn_tree.branches, val_tree.branches):
#         apply_tree(pair[0], pair[1])

def separate(separator, lnk):
    """Returns a new linked list (using Link) that separates
    any two consecutive repeated numbers in non-empty LNK
    by inserting a Link with the value of SEPARATOR.
    All values in LNK will be numbers.

    >>> separate(999, Link(1, Link(1)))     # Case 1: Separates list that starts with pair
    Link(1, Link(999, Link(1)))

    >>> separate(999, Link(1, Link(1, Link(1))))     # Case 2: Separates list with overlapping pairs
    Link(1, Link(999, Link(1, Link(999, Link(1)))))

    >>> link = Link(1, Link(1))     # Case 3: Doesn't mutate the input list
    >>> separate(999, link)
    Link(1, Link(999, Link(1)))
    >>> link
    Link(1, Link(1))

    >>> separate(-999, Link(2, Link(2, Link(4, Link(5)))))     # Case 4: Only separates pairs, not non-pairs
    Link(2, Link(-999, Link(2, Link(4, Link(5)))))

    >>> separate(-1, Link(2, Link(3, Link(4, Link(4)))))        # Case 5: Separates pairs at end of list
    Link(2, Link(3, Link(4, Link(-1, Link(4)))))

    >>> separate(999, Link(1, Link(2)))     # Case 6: Returns same-valued list if no pairs found
    Link(1, Link(2))

    >>> lnk = Link(1)      # Case 7: Handles single element lists correctly
    >>> lnk2 = separate(999, lnk)
    >>> lnk
    Link(1)
    >>> lnk is not lnk2
    True
    """
    if lnk.rest is Link.empty:
        rest = Link.empty
    elif lnk.first != lnk.rest.first:
        rest = separate(separator, lnk.rest)
    elif lnk.first == lnk.rest.first:
        orig_rest = lnk.rest
        rest  = Link(separator, separate(separator, orig_rest))
    return Link(lnk.first, rest)

# def rev(lnk):
#     """Yield the elements in Link instance s in reverse order.
#     >>> list(rev(Link(1, Link(2, Link(3)))))
#     [3, 2, 1]
#     >>> next(rev(Link(2, Link(3))))
#     3
#     """
#     if lnk is not Link.empty:
        
#         yield _____________________________________________________________________________

def stretch(s, repeat=0):
    """Replicate the kth element k times, for all k in s.
    >>> a = Link(3, Link(4, Link(5, Link(6))))
    >>> stretch(a)
    >>> print(a)
    <3, 4, 4, 5, 5, 5, 6, 6, 6, 6>
    """
    if s is not Link.empty:
        for i in range(repeat):
            new_value, original_rest = s.first, s.rest
            s.rest = Link(new_value, original_rest)
        return stretch(s.rest, repeat + 1)

def splink(a, b, k):
    """Return a Link containing the first k elements of a, then all of b, then the rest of a.
    >>> splink(Link(2, Link(3, Link(4, Link(5)))), Link(6, Link(7)), 2)
    Link(2, Link(3, Link(6, Link(7, Link(4, Link(5))))))
    """
    if b is Link.empty:
        return a
    elif k > 0:
        return Link(a.first, splink(a.rest, b, k-1))
    return Link(b.first, splink(a, b.rest, k - 1))

def pascal_row(s):
    """
    >>> a = Link.empty
    >>> for _ in range(5):
        ... a = pasal_row(a)
        ... print(a)
    <1>
    <1 1>
    <1 2 1>
    <1 3 3 1>
    <1 4 6 4 1>
    """
    if s is Link.empty:
        return Link(1)
    start = Link(1)
    last, current = start, s
    while current.rest is not Link.empty:
        start = Link(current.first + current.rest.first, start)
        current = current.rest
    start = Link(1, start)
    return start

def replicate_links(s):
    def replicate(repeat, s):
        if repeat > 0 and s.first > 0:
            return Link(s.first, replicate(repeat - 1, s))
        elif s.rest is Link.empty:
            return Link.empty
        return replicate(s.rest.first, s.rest)
    return replicate(s.first, s)