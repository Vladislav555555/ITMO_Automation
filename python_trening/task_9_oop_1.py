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

С1 = Class1(" Class1")
С2 = Class2(" Class2")
С3 = Class3(" Class3")
С4 = Class4(" Class4")

print(С1.check_text())
print(С2.check_text())
print(С3.check_text())
print(С4.check_text())