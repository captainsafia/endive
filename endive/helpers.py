# The unique, intersect, and union functons are sourced from
# http://www.saltycrane.com/blog/2008/01/how-to-find-intersection-and-union-of/
def unique(elements):
    """
    Removes duplicate elements from a list of elements.
    """
    return list(set(elements))

def intersect(a, b):
    """
    Identifies the elements in A that are in B.
    """
    return list(set(a) & set(b))

def union(a, b):
    """
    Identifies the elements that are in A or B or in both.
    """
    return list(set(a) | set(b))

def all_in(a, b):
    """
    Returns True if all the elements in A are in B. 
    """
    return len(intersect(a, b)) == len(a)
