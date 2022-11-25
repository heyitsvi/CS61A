

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


def link_expression(s):
    if s.rest is Link.empty:
        rest = ''
    else:
        rest = ', ' +  link_expression(s.rest)
    return f'Link({s.first}{rest})'

Link.__repr__ = link_expression

def check(s,v):
    if s == Link.empty:
        return False
    if s.first == v:
        return True
    else:
        return check(s.rest,v)

# def add(s,v):
#     #add v to s if v doesn't exist
#     if v == Link.empty or check(s,v) == True:
#         return s
#     else:
#         if s.rest is Link.empty:
#             s.rest = Link(v)
#         else:
#             return add(s.rest,v)
def add(s,v):
    assert s is not Link.empty

    if s.first > v:
        s.rest = Link(s.first, s.rest)
        s.first = v
    elif s.first < v and s.rest == Link.empty:
        s.rest = Link(v)
    elif s.first < v:
        add(s.rest,v)
    return s 

def link_map(fn, link):
    if link is Link.empty:
        return Link.empty
    else:
        return Link(fn(link.first), link_map(fn, link.rest))

def link_filter(fn, link):
    if link is Link.empty:
        return link
    else:
        if fn(link.first):
            return Link(link.first, link_filter(fn, link.rest))
        else:
            return link_filter(fn, link.rest)

def check_order(link):
    if link.rest is Link.empty:
        return True             
    else:
        if abs(link.first) <= abs(link.rest.first):
            return check_order(link.rest)
        else:
            return False

def sum_linked_list(link):
    if link is Link.empty:
        return 0
    else:
        return link.first + sum_linked_list(link.rest)

def multiple_links(lst):
    result = 1

    for l in lst:
        if l is Link.empty:
            return Link.empty
        result *= l.first
    new_lst = [l.rest for l in lst]
    return Link(result,multiple_links(new_lst))

def flip_two(link):
    if link.rest is Link.empty:
        return Link.empty
    else:
        link.rest.first, link.first = link.first, link.rest.first
        try:
            return flip_two(link.rest.rest)
        except:
            return Link.empty