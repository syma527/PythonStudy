import logging


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("zhangsan", 30)

print(getattr(p,"age"))
setattr(p,'age',41)
print(p.age)


print(hasattr(p,"name"))


print(delattr(p,'name'))
logging.log(logging.ERROR,"hello")