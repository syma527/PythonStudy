"""


"""


class Demo:
    def __enter__(self):
        print("自动执行")



    def test01(self):
        print("test01")

    def __exit__(self, exc_type, exc_value, traceback):
        # 类似后置处理器
        try:
            print("自动执行")
        except Exception as e:
            print(f"在退出时发生异常：{e}")

with Demo() as t:
    print(t)