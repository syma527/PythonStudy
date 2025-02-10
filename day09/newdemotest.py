def test01(x):
    return x * 2


result = map(test01, [3, 5, 7])
print(list(result))
