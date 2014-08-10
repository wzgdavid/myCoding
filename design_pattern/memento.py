# encoding:gb2312

'''
备忘录模式
'''


class Status:
    def __init__(self, hp, exp):
        self.hp = hp
        self.exp = exp


class Player:
    def __init__(self, status):
        self.setStatus(status)

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def creaMemento(self):
        self.memento = Memento(self.getStatus())
        return self.memento

    def restoreMemento(self, memento):
        self.setStatus(memento.getStatus())


class Memento:
    def __init__(self, status):
        self.status = status

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status


class CareTaker:
    def setMemento(self, memento):
        self.memento = memento

    def getMemento(self):
        return self.memento


p = Player(Status(500, 12345))
ct = CareTaker()
ct.setMemento(p.creaMemento())
p.setStatus(Status(100, 12345))
print(p.getStatus().hp)
p.restoreMemento(ct.getMemento())
print(p.getStatus().hp)
