from oops_concept.multi_level_inheritance.Vehicle import Vehicle


class Bike(Vehicle):
    def __init__(self,brand,model,year):
        super().__init__(model,year)
        self.brand = brand
    def display(self):
        super().display()
        print(self.brand)