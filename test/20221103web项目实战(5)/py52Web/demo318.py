"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/11/3 20:13
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
测试开内容：
内存管理：标记清除、分代回收、引用技术

一、深浅拷贝
1、目的：应付面试，实际工作中没有什么使用场景

2、浅拷贝：只拷贝一层目录,不会递归拷贝
test_dict = {"key1":"val1","key2":"val2","key3":[1,2]}
#拷贝test_dict
new_dict = test_dict.copy()
#修改test_dict里面的value
test_dict["key3"].append(333)
print(new_dict)
print(id(new_dict))
print("="*30)
print("原字典：")
print(test_dict)
print(id(test_dict))

3、深拷贝：深拷贝拷贝所有目录
import copy
test_dict = {"key1":"val1","key2":"val2","key3":[1,2]}
print("原字典：")
print(test_dict)
print(id(test_dict))
print("="*30)
#拷贝test_dict
new_dict = copy.deepcopy(test_dict)
#修改test_dict里面的value
test_dict["key3"].append(333)
print(new_dict)
print(id(new_dict))
print("="*30)
print("原字典：")
print(test_dict)
print(id(test_dict))

4、深拷贝只对可变容器类型而言才有意义
"""

import copy
test_dict = {"key1":"val1","key2":"val2","key3":[1,2]}
print("原字典：")
print(test_dict)
print(id(test_dict))
print("="*30)
#拷贝test_dict
new_dict = copy.deepcopy(test_dict)
#修改test_dict里面的value
test_dict["key3"].append(333)
print(new_dict)
print(id(new_dict))
print("="*30)
print("原字典：")
print(test_dict)
print(id(test_dict))






