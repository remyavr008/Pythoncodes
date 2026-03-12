class Greet:
    def greeting(self,name=None): #default function or function with default values
        if name:
            print("hello1",name)
        else:
            print("hello2")
greet = Greet()
greet.greeting("Remya")
