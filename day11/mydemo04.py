"""



class TestDemo:
    name = "老王"

    def test_01(self):
        print(self.name)

# if __name__ == '__main__':
#     cl = TestDemo()
#     cl.test_01()
#



class Student:
    school = "xcxy"  # 类属性
    __major = "computer"  # 私有属性

    def __init__(self, name, age):  # 构造方法
        self.name = name  # 实例属性
        self.__age = age  # 实例私有属性

    def match(self, score):  # 实例方法
        print(self.school)  # 访问类属性      self.类属性名
        print(Student.school)  # 访问类属性      类名.类属性名
        print(self.__major)  # 访问类私有属性    self.类私有属性名
        print(Student.__major)  # 访问类私有属性    类名.类私有属性名
        print(self.name)  # 访问实例属性      self.实例属性名
        print(self.__age)  # 访问实例私有属性   self.实例私有属性名

    def __fly(self, private_method):
        print("这是一个私有方法")  # 其他和实例方法相同

    @classmethod
    def eat(cls, num):  # 类方法
        print(cls.school)  # cls.类属性
        print(Student.school)  # 类.类属性
        print(cls.__major)  # cls.类私有属性
        print(Student.__major)  # 类名.类私有属性

    @staticmethod
    def run(numm):
        print(Student.school)  # 类名.类属性
        print(Student.__major)  # 类名.__私有类属性

stu = Student("hjh",24)  # 实例化对象

stu.school = "tsinghua"
print(stu.school)
Student.school = "beijing "
print(Student.school)


print(stu._Student__major)   # 对象._类名__私有属性名
print(Student._Student__major)  # 类名._类名__私有属性名

stu._Student__major = "jixie"
print(stu._Student__major)

Student._Student__major = "dianqi"
print(Student._Student__major)


print(stu.name)  # 对象.实例属性名
stu.name = "hsf"  # 修改对象属性名
print(stu.name)

print(stu._Student__age)  # 对象.实例属性名

"""


class Student:
    school = "beijing"
    __major = "computer"

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def match(self, score):  # 实例方法
        print(self.school)  # 访问类属性
        print(Student.school)  # 访问类属性
        print(self.__major)  # 访问类私有属性
        print(Student.__major)  # 访问类私有属性
        print(self.name)  # 访问实例属性
        print(self.__age)  # 访问实例私有属性

    def __fly(self):
        print("这是一个私有方法")  # 其他和实例方法相同

    # stu1 = Student("zhangsan", 30)
    @classmethod
    def eat(cls, num):
        print(cls.school)  # cls.类属性
        print(Student.school)  # 类.类属性
        print(cls.__major)  # cls.类私有属性

    @staticmethod
    def run(numm):
        print(Student.school)
        print(Student.__major)


stu = Student("lisi", 34)

stu.school = "tsinghua"
print(stu.school)
Student.school = "beijing"
print(Student.school)

print(stu._Student__major)

stu._Student__major = "jixie"
print(stu._Student__major)
