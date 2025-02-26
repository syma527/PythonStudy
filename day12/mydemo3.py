class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} is barking.")

dog1 = Dog("旺财",3)

dog1.bark()
print(dog1.name)
print(dog1.age)