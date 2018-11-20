
class Base:
    def __init__(self):
        print("Base init")

    def foo(self):
        print('Base foo')


class Derived1(Base):
    def __init__(self):
        print("Derived1 init")
        Base.__init__(self)

    def foo(self):
        print("Derived1 foo")


class Derived2(Base):
    def __init__(self):
        print("Derived2 init")
        Base.__init__(self)

    def foo(self):
        print("Derived2 foo")


class Diamant(Derived1, Derived2):
    def __init__(self):
        Derived1.__init__(self)
        Derived2.__init__(self)

    def foo(self, cls):
        cls.foo(self)


a = Diamant()
a.foo(Derived1)
a.foo(Derived2)
a.foo(Base)
