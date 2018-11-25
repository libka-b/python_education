
class Parent:
    def __init__(self, name):
        self.parent_name = name

    def get_personal_info(self):
        return f"I'm parent and my name is {self.parent_name}"

    def print_fun(self):
        print("PARENT: Fun is when I turn on TV and watching movie with my husband")


class Child(Parent):
    def __init__(self, name, age, parent_name):
        Parent.__init__(self, parent_name)
        self.child_name = name
        self.age = age

    def get_personal_info(self):
        return f"I'm child, my name is {self.child_name}, my parent is {self.parent_name} and i'm {self.age} years old"

    def print_fun(self):
        super().print_fun()
        print("CHILD: Thats fine, but better is Sex & Drugs & Rock & Roll")


child = Child("Honza Beachboy", 28, "Samantha Boring")
child.print_fun()
