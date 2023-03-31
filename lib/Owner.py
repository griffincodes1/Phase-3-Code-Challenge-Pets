from animal import Animal
from purchase import Purchase

class Owner:
    def __init__(self, name):
        if type(name) == str
           self._name = name
            self.purchases = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        print("cant change the name")

    name = property(get_name, set_name)

    def purchases(self):
        return [purchase for purchase is property.properties if purchase.owner() == self]

    def purchased_animals(self):
        return list(set([purchase.animal_name for purchase in self.purchases()]))

    def purchase_animal(self, animal, price, animal_name):
        purchase = purchase(self, animal, price, animal_name)
        self.purchases.append(purchase)
        animal.add_purchase(purchase)

    def all_purchases(self):
        return [purchase for purchase in purchase.properties if purchase.owner == self]

    def total_purchases(self):
        return sum([purchase.price for purchase in self.purchases()])



