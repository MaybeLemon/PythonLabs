from random import randint


class Tomato:

    def __init__(self, index):
        self.states = ['Отсутствует', 'Цветение', 'Зеленый', 'Красный']
        self._index = index
        self._state = self.states[index]

    def grow(self):
        if self._index != 3:
            self._index += 1
            self._state = self.states[self._index]

    def is_ripe(self):
        if self._index == 3:
            return True
        return False

    def get_index(self):
        return self._index

    def get_state(self):
        return self._state


class TomatoBush:
    def __init__(self, kolvo):
        self.kolvo = kolvo
        self.tomatoes = [Tomato(randint(0, 3)) for i in range(self.kolvo)]

    def grow_all(self):
        for i in range(len(self.tomatoes)):
            self.tomatoes[i].grow()

    def all_are_ripe(self):
        for i in range(self.kolvo):
            if not self.tomatoes[i].is_ripe():
                return False
        return True

    def give_away_all(self):
        self.tomatoes = []

    def get_index(self, index):
        return self.tomatoes[index].get_index()

    def get_count(self):
        return len(self.tomatoes)

    def get_state(self, index):
        return self.tomatoes[index].get_state()


def knowledge_base():
    return ("У вас есть помидоры.\nВы должны работать, чтобы они выросли.\nКогда они вырастут, "
            "можете собирать урожай\n")


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            return True
        else:
            return False

    def get_index(self, index):
        return self._plant.get_index(index)

    def get_state(self, index):
        return self._plant.get_state(index)

    def get_count(self):
        return self._plant.get_count()

