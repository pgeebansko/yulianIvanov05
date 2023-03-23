class Okay:
    def __init__(self, name, num_1, num_2):
        self.name = name
        self.num_1 = num_1
        self.num_2 = num_2

    def sum(self):
        return self.num_1 + self.num_2

    def subtract(self):
        return self.num_1 - self.num_2

    def __str__(self):
        return self.name


okay_1 = Okay("test_1", 10, 5)
okay_2 = Okay("test_2", 20, 10)

print(okay_1)
print(okay_1.sum())
print(okay_1.subtract())
print(okay_2)
print(okay_2.sum())
print(okay_2.subtract())
