
class Parent:
    def __init__(self, name):
        self.parent_name = name

    def get_personal_info(self):
        return f"I'm parent and my name is {self.parent_name}"


class Child(Parent):
    def __init__(self, name, age, parent_name):
        Parent.__init__(self, parent_name)
        self.child_name = name
        self.age = age

    def get_personal_info(self):
        return f"I'm child, my name is {self.child_name}, my parent is {self.parent_name} and i'm {self.age} years old"


parent = Parent("Tonda Blanik")
print(parent.get_personal_info())

child = Child("Zizala", 28, "Big Tony")
print(child.get_personal_info())
