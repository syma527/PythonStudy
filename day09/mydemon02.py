func = lambda x,y:x+y
result = func(1,5)

test_list = [[1,33,5],[2,33,2],[53,34,2]]
test_list.sort(key = lambda x:x[1])
print(test_list)

test_dict = {"key1":"val1","key4":"val5","key2":"val3"}
result1 = sorted(test_dict.items(),key = lambda x:x[0],reverse=True)
print(result1)