from task_9_checks import Checks

class ClassA(Checks):
    def __init__(self, loc, other_param):
        super().__init__(loc)
        self.other_param = other_param

class ClassB(Checks):
    def __init__(self, loc, other_param):
        super().__init__(loc)
        self.other_param = other_param

class ClassC(Checks):
    def __init__(self, loc, other_param):
        super().__init__(loc)
        self.other_param = other_param

class ClassD(Checks):
    def __init__(self, loc, other_param):
        super().__init__(loc)
        self.other_param = other_param


if __name__ == "__main__":
    a = ClassA("Text from ClassA", 123)
    b = ClassB("Text from ClassB", 456)
    c = ClassC("Text from ClassC", 789)
    d = ClassD("Text from ClassD", 101112)

    print(a.check_text())  # Text from ClassA
    print(b.check_text())  # Text from ClassB
    print(c.check_text())  # Text from ClassC
    print(d.check_text())  # Text from ClassD