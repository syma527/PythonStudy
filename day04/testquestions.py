"""
基础操作题（1-6）编写代码，将变量 name = "Alice" 和 age = 25 拼接成字符串："Alice今年25岁"。
给定字符串 s = "  Hello World  "，去除两端空格后，再转换为全大写输出。
字符串 text = "Python is awesome"，用切片取出 "is" 这个单词。
字符串 path = "/Users/xiaoming/Documents/file.txt"，用切片取出文件名（含扩展名）"file.txt"。
判断字符串 email = "test@example.com" 是否包含 "@" 符号，并输出 True 或 False。
将字符串 s = "apple,banana,orange" 用逗号分割成列表，然后再用横线 - 连接成新字符串。

字符串方法题（7-12）给定字符串 s = "I love Python programming"，统计字母 "o" 出现了几次。
将字符串 s = "hello world" 的首字母大写，其他保持不变（标题化）。
字符串 s = "abc123def456"，替换所有数字为 ""，输出结果如 "abcdef*"。
检查字符串 password = "Abc12345" 是否同时包含大小写字母和数字（分别用 isupper(), islower(), isdigit() 判断）。
字符串 s = "   python   "，去除所有前后空格后，检查是否全部是小写字母。
给定字符串 s = "The quick brown fox"，将所有 "o" 替换为 "0"（零）。

字符串格式化题（13-16）使用 f-string 格式化输出：商品名 "MacBook"，价格 12999，输出 "MacBook 的价格是 12999 元"。
使用 format() 方法，将 pi = 3.14159 四舍五入保留两位小数，输出 "π ≈ 3.14"。
给定列表 fruits = ["apple", "banana", "cherry"]，用 join() 方法连接成 "apple - banana - cherry"。
使用 % 格式化（老式）输出：名字 "张三"，成绩 95.5 分，输出 "张三的成绩是95.5分"。

综合应用题（17-18）编写一个函数 reverse_string(s)，接收一个字符串参数，返回其反转后的字符串（例如 "hello" → "olleh"）。要求用切片实现。
编写一个函数 is_palindrome(s)，判断一个字符串忽略大小写和空格后是否是回文串（例如 "A man a plan a canal Panama" → True）。



# 第一题
name = "Alice"
age = 26

# res = f"{name} is {age} this year"
res = "{} is {} this year".format(name,age)
print(res)

# 第二题
s = "  Hello World   "

res2 = s.strip().upper()
print(res2)

# 第三题
# 字符串 text = "Python is awesome"，用切片取出 "is" 这个单词。
text = "Python is awesome"
res3 = text[7:9]
print(res3)

# 第四题 字符串 path = "/Users/xiaoming/Documents/file.txt"，用切片取出文件名（含扩展名）"file.txt"。
path = "/Users/xiaoming/Documents/file.txt"
res4 = path[25::]
print(res4)

# 第五题 判断字符串 email = "test@example.com" 是否包含 "@" 符号，并输出 True 或 False。
email = "test@example.com"
res5 = "@" in email
print(res5)

# 第六题 将字符串 s = "apple,banana,orange" 用逗号分割成列表，然后再用横线 - 连接成新字符串。
s = "apple,banana,orange"
res6 = ''.join(s)
res7 = res6.replace(',','-')
print(res7)

# 第七题 给定字符串 s = "I love Python programming"，统计字母 "o" 出现了几次
s = "I love Python programming"
res7 = s.count('o')
print(res7)

# 第八题 将字符串 s = "hello world" 的首字母大写，其他保持不变（标题化）。
s = "hello world"
res = s.title()
print(res)

# 第九题 字符串 s = "abc123def456"，替换所有数字为 ""，输出结果如 "abcdef*"。
s = "abc123def456"
import re
new_s = re.sub(r"[0-9]","",s)
print(new_s)

#? 第10题 检查字符串 password = "Abc12345" 是否同时包含大小写字母和数字（分别用 isupper(), islower(), isdigit() 判断）。
password = "Abc12345"

# 第11 题 字符串 s = "   python   "，去除所有前后空格后，检查是否全部是小写字母

s = "   python   "
res11 = s.strip().islower()
print(res11)

# 第12题 给定字符串 s = "The quick brown fox"，将所有 "o" 替换为 "0"（零）
s = "The quick brown fox"
res12 = s.replace("o","0")
print(res12)


# 第13题 使用 f-string 格式化输出：商品名 "MacBook"，价格 12999，输出 "MacBook 的价格是 12999 元"
product_name = "Macbook12"
price = 12999
str13 = f"{product_name} 's price is {price} yuan"
print(str13)

# 第14题 使用 format() 方法，将 pi = 3.14159 四舍五入保留两位小数，输出 "π ≈ 3.14"。

s = "π = {pi:.2f}".format(pi = 3.1415926)
print(s)

# 第15题 fruits = ["apple", "banana", "cherry"]，用 join() 方法连接成 "apple - banana - cherry"

fruits = ["apple","banana","cherry"]
res16 = '-'.join(fruits)
print(res16)



# 第16题 使用 % 格式化（老式）输出：名字 "张三"，成绩 95.5 分，输出 "张三的成绩是95.5分"

res16 = "%s 's grades is %.2f " %("zhangsan",95.5)
print(res16)

# 第17题 编写一个函数 reverse_string(s)，接收一个字符串参数，返回其反转后的字符串（例如 "hello" → "olleh"）。要求用切片实现
def reverse_string(s):
     r = s[::-1]
     return r


if __name__ == '__main__':
 re = reverse_string("hello")
 print(re)
"""

# 第18题 编写一个函数 is_palindrome(s)，判断一个字符串忽略大小写和空格后是否是回文串（例如 "A man a plan a canal Panama" → True）
s = "abc123def456"
new_s = ''.join(c if s.islower() else '*' for c in s)
new_s = ''.join(c if c.islower() else '*' for c in s)

print(new_s)