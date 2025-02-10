test_str = "{} price is {}".format("zhangsan",15)
print(test_str)

test_str1 = "{1} price is {0}".format("zhangsan",15)
print(test_str1)
test_str2 = "{name} say {something} is good {thing}".format(name="tom", something="apple",thing="fruit")

dog = "steve"
cat = "William"
friends = "pet"

test_str3 = f"{dog} and {cat} is my good {friends}"
print(test_str3)
