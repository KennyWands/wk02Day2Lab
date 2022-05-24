from src.bus import Bus


class BusStop:
    def __init__(
        self,
        get_name,
    ):
        self.name = get_name
        self.queue = []

    def queue_length(self):
        return len(self.queue)

    def add_to_queue(self, person):
        self.queue.append(person)

    def clear(self):
        self.queue.clear()

    def pick_up_from_stop(self, bus_stop):
        for person in bus_stop.queue:
            Bus.pick_up(person)
