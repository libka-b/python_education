
class Parent:
    def __init__(self, name):
        self.parent_name = name
        self.best_place = "My lovely couch"

    def get_personal_info(self):
        return f"I'm parent and my name is {self.parent_name}"

    def print_fun(self):
        print("Fun is when I turn on TV and watching movie with my husband")

    def print_my_best_place(self):
        print(self.parent_name, self.best_place)


class Child1(Parent):
    def __init__(self, name, age, parent_name):
        Parent.__init__(self, parent_name)
        self.child_name = name
        self.age = age
        self.best_place = "Nice library"

    def get_personal_info(self):
        return f"I'm child, my name is {self.child_name}, my parent is {self.parent_name} and i'm {self.age} years old"

    def print_fun(self):
        super().print_fun()
        print("Thats fine, but better is Sex & Drugs & Rock & Roll")

    def print_my_best_place(self):
        super().print_my_best_place()
        print(self.child_name, self.best_place)


class Child2(Parent):
    def __init__(self, name, age, parent_name):
        self.child_name = name
        self.age = age
        self.best_place = "Pub with a great beer"
        Parent.__init__(self, parent_name)

    def get_personal_info(self):
        return f"I'm child, my name is {self.child_name}, my parent is {self.parent_name} and i'm {self.age} years old"

    def print_fun(self):
        super().print_fun()
        print("Thats fine, but better is Sex & Drugs & Rock & Roll")

    def print_my_best_place(self):
        super().print_my_best_place()
        print(self.child_name, self.best_place)


child1 = Child1("Honza Beachboy", 28, "Samantha Boring")
child2 = Child2("Kuba Drunk", 28, "Samantha Boring")
child1.print_my_best_place()
print()
child2.print_my_best_place()
