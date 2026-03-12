class Vehicle:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    def display(self):
        print(self.model)
        print(self.year)