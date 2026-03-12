class Person:
    def __init__(self,name,age,password):
        self.name=name #public attribute.so it can be accessed anywhere in the package
        self._age=age  #protected attribute
        self.__password=password

    def set_password(self,password):
        self.__password=password
    def get_password(self):
        return self.__password

person1 = Person("remya",27,"newrem")
person1.name="Remya"
print(person1.name)

#print(person1.password) #error will be displayed
person1.set_password("remya1")
print(person1.get_password())
print(person1._age)