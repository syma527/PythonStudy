test_list = [1,33,45,6]
result = dict(list(enumerate(test_list)))

new_dict = {}

for key,val in result.items():
    print(key,val)
    new_dict[key] = val

print(new_dict)

