from task_9_checks import Checks


class Class1(Checks):
    def __init__(self, loc):
        super().__init__(loc)


class Class2(Checks):
    def __init__(self, loc):
        super().__init__(loc)


class Class3(Checks):
    def __init__(self, loc):
        super().__init__(loc)


class Class4(Checks):
    def __init__(self, loc):
        super().__init__(loc)


c1 = Class1("Class1")
c2 = Class2("Class2")
c3 = Class3("Class3")
c4 = Class4("Class4")

print(c1.check_text())
print(c2.check_text())
print(c3.check_text())
print(c4.check_text())