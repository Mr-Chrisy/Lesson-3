class Student:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self, cm):
        self.height += cm
        print(f"{self.name} виріс, зріст, {self.height}")

    def __str__(self):
        return f"Студент {self.name}, йогозріст - {self.height}"

    def __del__(self):
        print (f"Студент {self.name}видалено!")
Bob = Student("Bob", 150)
Kate = Student("Kate", 130)

Bob.grow(10)
print(Bob)

