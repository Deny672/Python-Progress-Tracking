class Cat:
    def __init__(self, name):
        self.name = name

    # __repl__ makes an output of debugging information
    def __repr__(self):
        return f"{self.__class__}: {self.name}"

    # __str__ makes the output of information to the user
    def __str__(self):
        return f"{self.name}"

cat = Cat("Audi A8 D2")
print(str(cat))
print(cat)