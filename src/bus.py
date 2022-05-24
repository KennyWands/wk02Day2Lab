class Bus:
    def __init__(self, get_route, get_destination):
        self.route_number = get_route
        self.destination = get_destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def pick_up(self, person):
        self.passengers.append(person)

    def drop_off(self, person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop):
        for person in bus_stop.queue:
            self.pick_up(person)