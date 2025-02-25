class Demo:
    color = "red"
    @classmethod
    def set_color(cls, new_color):
        cls.color = new_color

    @classmethod
    def test_10(cls):
        print("test_01类方法")
        cls.test_04()

    @classmethod
    def test_04(cls):
        print(f"Color is: {cls.color}")

Demo.set_color("blue")

cl = Demo()
cl.test_10()

cl.set_color("green")
Demo().test_10()