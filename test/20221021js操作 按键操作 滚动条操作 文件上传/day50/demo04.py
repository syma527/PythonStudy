"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 20:34
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
十三、document对象
1、什么是document对象
	1、每个载入浏览器的HTML文档都会成为 Document 对象。
	2、Document对象使我们可以从脚本中对 HTML页面中的所有元素进行访问。
	
2、document对象常用方法                   
	1、查找元素
		ele1 = document.getElementById("kw")
		ele1.value="柠檬班"
		ele2 = document.getElementById("su")
		ele2.click()
	2、修改元素属性
		ele.value="柠檬班"
		
3、document对象其他方法
	1、getElementsByClassName(): 返回文档中所有指定类名的元素集合，作为 NodeList 对象。
	2、getElementById():返回对拥有指定 id 的第一个对象的引用。
	3、getElementsByName():返回带有指定名称的对象集合。
	4、getElementsByTagName():返回带有指定标签名的对象集合。
	5、addEventListener():向文档添加句柄
	6、adoptNode(node)	从另外一个文档返回 adapded 节点到当前文档。
	7、close():关闭用document.open()方法打开的输出流，并显示选定的数据。
	8、createAttribute(): 创建一个属性节点
	9、createDocumentFragment():创建空的 DocumentFragment 对象，并返回此对象。
	10、createElement():创建元素节点。
	11、createTextNode():创建文本节点。
	12、importNode():把一个节点从另一个文档复制到该文档以便应用。
	13、normalize():删除空文本节点，并连接相邻节点
	14、normalizeDocument():删除空文本节点，并连接相邻节点的
	15、open():打开一个流，以收集来自任何 document.write() 或 document.writeln() 方法的输出。
	16、querySelector():返回文档中匹配指定的CSS选择器的第一元素
	17、querySelectorAll():HTML5中引入的新方法，返回文档中匹配的CSS选择器的所有元素节点列表
	18、removeEventListener():移除文档中的事件句柄(由 addEventListener() 方法添加)
	19、renameNode():重命名元素或者属性节点。
	20、write():向文档写 HTML 表达式 或 JavaScript 代码。
	21、writeln():等同于 write() 方法，不同的是在每个表达式之后写一个换行符。



"""