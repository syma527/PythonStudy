def sum_num(name,age,*args,**kwargs):
    print(f"Name: {name}, Age: {age}")
    print(f"额外位置参数 args: {args}")
    print(f"额外关键字参数 kwargs: {kwargs}")

test_dict = {"first_name": "法外狂徒张三", "last_names":"老王"}
test_list = [90,89]

sum_num("老王", 40, *test_list, **test_dict)
