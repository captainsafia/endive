from endive.event import Event
import datetime

def test_same_event():
    this = Event([1,2,3,4], datetime.datetime(2015, 3, 5, 0, 0))
    same = Event([1,2,3,4], datetime.datetime(2015, 3, 5, 0, 0))
    different_data = Event([5,6,7,8], datetime.datetime(2015, 3, 5, 0, 0))
    different_date = Event([1,2,3,4], datetime.datetime(2014, 3, 5, 0, 0))
    different = Event([9,10,11,12], datetime.datetime(2016, 4, 5, 0, 0))
    assert this.same_event(same) == True
    assert this.same_event(different_data) == False
    assert this.same_event(different_date) == False
    assert this.same_event(different) == False

def test_preceding():
    this = Event([1,2,3,4], datetime.datetime(2015, 3, 5, 0, 0))
    before = Event([1,2,3,4], datetime.datetime(2015, 3, 4, 0, 0))
    after = Event([1,2,3,4], datetime.datetime(2015, 3, 6, 0, 0))
    assert this.preceding(before) == False
    assert this.preceding(after) == True

def test_seceding():
    this = Event([1,2,3,4], datetime.datetime(2015, 3, 5, 0, 0))
    before = Event([1,2,3,4], datetime.datetime(2015, 3, 4, 0, 0))
    after = Event([1,2,3,4], datetime.datetime(2015, 3, 6, 0, 0))
    assert this.seceding(before) == True
    assert this.seceding(after) == False
