import helpers

class Event():
    def __init__(self, data):
        self.data = data

    def same_event(self, other):
        return self.data == other.data
