def multiply_numbers():
    try:
        # 获取用户输入并转换为浮点数
        a = float(input("请输入第一个数字: "))
        b = float(input("请输入第二个数字: "))

        # 计算乘积
        result = a * b

        # 格式化输出结果
        test_int = f"{a} multiply {b} is {result}"
        print(test_int)
    except ValueError:
        print("输入无效，请输入数字。")


# 调用函数
multiply_numbers()
