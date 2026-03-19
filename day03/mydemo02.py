"""
import  random

caiquan = input('请输入石头剪刀布')

computer= random.choice(['石头','剪刀','布'])

if (caiquan == '石头' and computer == '剪刀') or (caiquan == '剪刀' and computer == '布')or (caiquan == '布' and computer == '石头'):

    print(computer,"你赢了")
elif caiquan == computer:
    print(computer,"平局")
else :
    print(computer,'你输了')


a = 'sixstar'

print(a)

a1 = a.encode()
print(a1)



name = 'class_name_sixstar'

a = name[0]
b = name[1]
c = name
print(a,b,c)


print(name[6:10:1]) #n m



a = 'hello world'

print(a.find('h'))
print(a.find('hello'))
print(a.find('e',0,5))

str_001 = []
"""

# index查找索引
# 与find 方法一样,只不过如果str不在mystr中会报一个异常
# mystr = 'hello world'
# target = 'l'
# indices =  [i for i,char in enumerate(mystr) if char == target]
# print(indices)


# mystr = 'hello world'
# print(mystr.replace('l','e'))
# print(mystr.replace('l','k',2))# (旧子串,新子串,替换次数)

#
# a = 'hello,python'
#
# s = a.capitalize()
# s01 = a.title()
# print(s)
# print(s01)


# a = 'HEEELo'
# print(a.swapcase())
# print(a.upper())


"""str_001 = r'Hello\beijing\tianqiao'
print(str_001)

str_002 = 'HEEEW'
print(str_002.isupper())



j = 0
mystr = 'hello123'
for i in mystr:
    if i.isdigit():
        j +=1

print(j)

"""


a = ' hello 123'
a.strip()
print(a)
