class Purchase:
    properties = []
    def __init__(self, owner, animal, price, animal_name)
        if type(price) == float:
            self._price = price
        if type(animal_name) == str:
            self.animal_name = animal_name
        self.owner = owner
        self.animal = animal

        Purchase.properties.append(self)

   
    def get_price(self):
        return self._price

    def set_price(self, price):
        print("cannot change")

    price = property(get_price,  set_price)


    def get_animal_name(self):
        return self._animal_name

    def set_animal_name(self, animal_name):
        animal_name = self.animal_name

    animal_name = property(get_animal_name, set_animal_name)

    
    def owner(self):
        return self.owner

    def animal(self)
        return self.animal

       
        