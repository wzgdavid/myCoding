# encoding: utf-8


class Component:
    def __init__(self, name):
        pass

    def Add(self, com):
        pass

    def remove(self, com):
        pass

    def __str__(self):
        return self.nodeName


class Leaf(Component):
    def __init__(self, name):
        self.nodeName = name

    def Add(self):
        print("leaf can't add")

    def remove(self):
        print("leaf have nothing to remove")

    def __str__(self):
        return 'this is a leaf : '.join(self.nodeName)


class Composite(Component):
    def __init__(self, name):
        self.components = []
        self.nodeName = name

    def Add(self, component):
        if self != component:
            self.components.append(component)
        else:
            print('can not add self')

    def remove(self, component):
        self.components.remove(component)

    def __str__(self):
        return 'this is a Composite : '+self.nodeName

    def showChildren(self):
        for com in self.components:
            print(com)


leaf = Leaf('leaf 1')
leaf2 = Leaf('leaf 2')
com = Composite('Composite 1')
com2 = Composite('Composite 2')
com.Add(leaf)
com.Add(leaf2)
com.Add(com2)
com.showChildren()
