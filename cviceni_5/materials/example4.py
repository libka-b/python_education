
class Mother:
    def __init__(self, eyes, hair_color, legs, fingers):
        self.eyes = eyes
        self.hair_color = hair_color
        self.__legs = legs
        self.__fingers = fingers

    def be_sexy(self):
        print("Hi chickas, wanna some drink?")


class Father:
    def __init__(self, eyes, hair_color, legs, fingers):
        self.__eyes = eyes
        self.__hair_color = hair_color
        self.legs = legs
        self.fingers = fingers

    def drink_beer(self):
        print("Give me beer and write it by rake")


class Child(Mother, Father):
    def __init__(self, age, name):
        Mother.__init__(self, 'blue', 'black', 1, 13)
        Father.__init__(self, 'brown', 'blond', 2, 10)
        self.age = age
        self.name = name

    def introduce_yourself(self):
        print(f"Hi, i'm {self.name}, i'm {self.age} years old")
        print(f"I have {self.eyes} eyes and {self.hair_color} hair")
        print(f'I have {self.legs} legs and {self.fingers} fingers')


child = Child(28, "Johny Licker")
child.introduce_yourself()