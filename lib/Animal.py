class Animal:
    def __init__(self, name, type):
        if type(name) == str:
            self._name = name
        if type(type) == str:
            self._type = type
        self.purchases = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        print("cannot change")

    name = property(get_name, set_name)

    def get_type(self):
        return self._type

    def set_type(self, type):
        print("cannot change type")

    type = property(get_type, set_type)

    def owners(self):
        return list(set(purchase.owner() for purchase in self.purchases))

    def animal_names(self):
        purchases = [purchase for purchase in purchase.properties if purchase.animal == self]
        return list(set([purchase.animal_name for purchase in purchases]))

    def biggest_enthusiast(self):
        purchases = [purchase for purchase in purchase.properties if purchase.animal == self]
        owners = [purchase.owner for purchase in purchases]
        return max(set(owners), key=owners.count).getname()

