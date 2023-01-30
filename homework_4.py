class Inheritance_1:
    def __init__(self, name):
        self.name = name

class Inheritance_2(Inheritance_1):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
class Inheritance_3:
    def show2(self):
        print("3")

class Inheritance_4:
    def show3(self):
        print("4")

class Main_inheritance(Inheritance_2, Inheritance_3, Inheritance_4):
    def __init__(self, name, age):
        super().__init__(name, age)

    def show1(self):
        print(f"Имя: {self.name}\n"
              f"Возраст: {self.age}")

a = Main_inheritance("Asyl", 22)
a.show1()
a.show2()
a.show3()