# python反射==动态设置属性

1、设置属性

可以给类设置属性，也可以给类实例设置属性、修改属性、判断属性、删除属性

setattr(类名称/或者实例名称，属性名称，属性值)



2、获取属性

getattr(类名称/或者实例名称,属性名称，默认值)

如果不设置默认值，当key不存在的时候会报错



3、判断属性

hasattr(类名称或者实例名称, 属性名称)

属性存在时返回true，否则返回false



4、删除属性

delattr(类名称或者实例名称, 属性名称)

```
class Demo:
	"""多行注释"""
	pass
if __name__ == '__main':
	cl = Demo()
	print(cl.__dict__)
	setattr(cl,"python","52期")
	result = getattr(cl,"pyt","50期")
	print(result)
	print(cl.__dict__)
	res2 = hasattr(cl,"python")
	print(res2)
	delattr(cl,"python")
	print(cl.__dict__)
```

