from endive.event import Event

def test_same_event():
    this = Event([1,2,3,4])
    same = Event([1,2,3,4])
    different = Event([5,6,7,8])
    assert this.same_event(same) == True
    assert this.same_event(different) == False
