from oops_concept.Hierarchial_inheritance.Vehicle import Vehicle


class Car(Vehicle):
    def vehicledetails(self):
        super().vehicledetails()#if want to access from parent class
        print("car is a  4wheeler")
car1 = Car()
car1.vehicledetails()
car1.vehiclefeatures()
