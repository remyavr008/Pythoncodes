from oops_concept.multi_level_inheritance.bike import Bike


class Motorbike(Bike):
    def __init__(self,color,brand,model,year):
        super().__init__(brand, model, year)
        self.color = color
    def display(self):
        super().display()
        print(self.color)
heroHonda=Motorbike("blue","Honda","1991",2026)
heroHonda.display()

