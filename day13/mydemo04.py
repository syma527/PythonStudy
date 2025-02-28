import  time

def timer_docorator(func):
    def wrapp():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"函数执行耗时{end_time - start_time:.2f}秒")

    return wrapp
@timer_docorator
def test_01():
    time.sleep(9)
    print("函数执行完毕")

test_01()
