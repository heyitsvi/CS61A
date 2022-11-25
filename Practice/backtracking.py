# def permutations(lst):
#     if len(lst) == 1:
#         return [lst[:]]
    
#     perms = permutations(lst[1:]) # 'abc' --> 'bc' --> 'c' 

#     first_element = [lst[0]]

#     result = []

#     for i in range(len(lst)):
#         for perm in perms:
#             result.append(perm[:i] + first_element[0:1] + perm[i:])

#     return result

# def all_perms(elements):
#     if len(elements) <=1:
#         yield elements
#     else:
#         for perm in all_perms(elements[1:]):
#             for i in range(len(elements)):
#                 # nb elements[0:1] works in both string and list contexts
#                 yield perm[:i] + elements[0:1] + perm[i:]
    
# def neetcode(lst):
#     result = []

#     #base case
#     if len(lst) == 1:
#         return [lst[:]]

#     for i in range(len(lst)):
#         first_element = lst.pop(0)

#         perms = neetcode(lst)
#         print(perms)
#         for perm in perms:
#             perm.append(first_element)

#         result.extend(perms)

#         lst.append(first_element)
    
#     return lst



def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        perms = all_perms(elements[1:])
        print(perms)
        for perm in perms:
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]