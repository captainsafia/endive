import helpers

class Event():
    def __init__(self, data, timestamp):
        self.data = data
        self.timestamp = helpers.convert_to_epoch(timestamp)

    def same_event(self, other):
        return self.data == other.data and self.timestamp == other.timestamp

    def preceding(self, other):
        return self.timestamp < other.timestamp

    def seceding(self, other):
        return self.timestamp > other.timestamp
