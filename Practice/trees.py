class Tree:
    def __init__(self ,label ,branches = []):
        self.label = label
        for b in branches:
            assert isinstance(b, Tree)
        self.branches = branches

    def is_leaf(self):
        return self.branches == []

def make_even(t):
    # if t.branches == []:
    #     return []    
    if t.label % 2 == 1:
        t.label += 1
    for b in t.branches:
        make_even(b)
    return t

def leaves(t):
    if t.is_leaf():
        return [t.label]
    else:
        result = [leaves(b) for b in t.branches]
    return sum(result,[])

def find_paths(t, entry):
    if t.label == entry:
        return [t.label]
    paths = [find_paths(b, entry) for b in t.branches]
    print(paths)
    for path in paths:
        if path:
            return [t.label] + path
