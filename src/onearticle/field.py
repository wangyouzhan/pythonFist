class Programer(object):
    hobby = 'Paly Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight


if __name__ == '__main__':
    programer = Programer('Alber', 25, 80)
    print
    dir(programer)
    print
    programer.__dict__
    print
    programer.get_weight()
    print
    programer._Programer__weight





















