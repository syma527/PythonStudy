class Demo:
    def __enter__(self):
        #类似前置处理器
        print("调用类的时候自动执行的方法")
        return self

    def __exit__(self,exc_type, exc_val, exc_tb):
        #类似后置处理器
        print("执行完成退出的时候会自动执行的方法")


    def test01(self):
        print("干活的人")
if __name__ == '__main__':
    with Demo() as t:
        print(t)
        t.test01()