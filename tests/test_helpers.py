import endive.helpers as helpers

def test_unique():
    items = [1,1,2,2,2,3,4,5,6,6,6,3,3,2]
    unique_items = [1,2,3,4,5,6]
    assert helpers.unique(items) == unique_items

def test_intersect():
    a = [1,2,3,4,5,6,7,8]
    b = [6,7,8,9,10,11,12]
    a_b_intersect = [8, 6, 7]
    assert helpers.intersect(a, b) == a_b_intersect

def test_union():
    a = [1,2,3,4,5,6,7,8,5,5,4]
    b = [6,7,8,9,10,12,12,12]
    a_b_union = [1,2,3,4,5,6,7,8,9,10,12]
    assert helpers.union(a, b) == a_b_union

def test_all_in():
    a = [1,2,3,4]
    b = [1,2,3,4,5,6,7]
    c = [7,8,9,10]
    assert helpers.all_in(a, b) == True
    assert helpers.all_in(c, b) == False
