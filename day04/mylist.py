"""test_os  = '%s say today is nice day %s' % ('laowang',123)
print(test_os)


str_002 = '%s price is %d' % (123,345)
print(str_002)"""

"""test_str_001 = '{price} price is {name:s}'.format(name= "iphone23",price= 234.03345)
print(test_str_001)"""

name = 'iphone123'

price = 10

num = 50
test_str = f'{name:} price is {price:.2f} and {price +num}'
print(test_str)