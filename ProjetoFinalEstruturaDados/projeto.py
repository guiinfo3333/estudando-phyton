values_permited = ['M', 'G', 'C']

class SystemParking:
    def __init__(self):
        self._list_spaces_automobile = []
        self._available_quantity_motorcycles = 0
        self._available_quantity_small_cars = 0
        self._available_quantity_big_cars = 0

    def __str__(self):
        return self._list_spaces_automobile.__str__()

    def insert_list_spaces_automobile(self, space):
        self._list_spaces_automobile.append(space)

    def verify_quantities_motorcyles(self):
        qtd = 0
        for result in self._list_vehicles:
            qtd += 1
        self._available_quantity_motorcycles = qtd

    def verify_quantity_small_cars(self):
        qtd = 0
        for result in self._available_quantity_small_cars:
            qtd += 1
        self._available_quantity_small_cars = qtd

    def verify_quantity_big_cars(self):
        qtd = 0
        for result in self._available_quantity_big_cars:
            qtd += 1
        self._available_quantity_big_cars = qtd

    def park(self):
        print("park")

    def exit(self):
        print("park")

    def report(self):
        print("report")

class Automobile:
    def __init__(self, board, free, type):
        self._board = board  #placa do carro
        self._free = free
        self._type = type
        if type is not values_permited:
            raise NameError("the values for the attribute 'type' must be \"M\",\"G\",\"C\"")


class SpacesAutomobile:
    def __init__(self, id, free, type):
        self._id = id
        self._free = free
        self._type = type
        if (not type in values_permited):
            raise NameError("the values for the attribute 'type' must be \"M\",\"G\",\"C\"")


if __name__ == '__main__':
    system = SystemParking()
    for index in range(1, 101):
        if index > 0 and index < 26:
            spaces_automobiles = SpacesAutomobile(index, True, "M")
        elif index > 25 and index < 51:
            spaces_automobiles = SpacesAutomobile(index, True, "G")
        else:
            spaces_automobiles = SpacesAutomobile(index, True, "C")
        system.insert_list_spaces_automobile(spaces_automobiles)

    print(system._list_spaces_automobile)

