from collections.abc import Iterable

test_str = "python123"

result = isinstance(test_str, Iterable)

print(result)
num = 0
while num < 10:
    print(f"num is {num}")
    num += 1
print("end")
