from oops_concept.Hierarchial_inheritance.Vehicle import Vehicle


class Bike(Vehicle):
    def vehicledetails(self):
        super().vehicledetails()#To print from parent class without overriding
        print("bike is a 2 wheeler")
Hero = Bike()
Hero.vehiclefeatures()
Hero.vehicledetails()