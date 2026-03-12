from oops_concept.multiple_inheritanc.Father import Father
from oops_concept.multiple_inheritanc.Mother import Mother


class Child(Mother,Father):
    def skills(self):
        super().skills()
        print("Child Plays")
child1 = Child()
child1.skills()

