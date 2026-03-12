from oops_concept.single_level_inheritance.Vehicle import Vehicle


class Car(Vehicle):
    def __init__(self,color,mileage,model,year):
        super().__init__(model,year) #super keyword is used to acquire something from the parent class
        self.color =color
        self.mileage =mileage

    def display(self):
        super().display() #method overriding
        print(self.color)
        print(self.mileage)
car1 = Car("Red",1000,"BMW",2026)
car1.display()
print("end")