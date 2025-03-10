"""
============================
Project: py52
Author:柠檬班-海励
Time:2022/10/21 20:13
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
"""
链式调用的原理
1、ActionChains类里面每个方法返回的都是ActionChains类的实例
2、类里面的方法调用方式就是通过类实例调用的，所以可以在方法后面直接调用ActionChains类里面的方法
3、本质上还是类实例调用实例方法
action.drag_and_drop_by_offset(source=source,xoffset=loc["x"],yoffset=loc["y"]+50).perform()

获取当前元素的坐标(元素坐标： {'x': 8, 'y': 8})
source = dr.find_element_by_xpath('//div[@id="draggable"]')
loc = source.location


1、action.perform(self)：执行鼠标操作方法
2、action.reset_actions()：清楚操作子令
3、action.click(on_element=None)：点击鼠标左键
4、action.click_and_hold(on_element=None)：点击鼠标左键，不松开
5、action.context_click(on_element=None)：点击鼠标右键
6、action.double_click(on_element=None)：双击鼠标左键
7、action.drag_and_drop(source, target)：拖拽到某个元素然后松开
8、action.drag_and_drop_by_offset(source, xoffset, yoffset)：拖拽到某个坐标然后松开
9、action.key_down(value, element=None)：按下某个键盘上的键
10、action.key_up(value, element=None)：松开某个键
11、action.move_by_offset(xoffset, yoffset)：鼠标从当前位置移动到某个坐标
12、action.move_to_element(to_element)：鼠标移动到某个元素
13、action.move_to_element_with_offset(to_element, xoffset, yoffset)：
    移动到距某个元素（左上角坐标）多少距离的位置
14、action.pause(seconds)：暂停操作(秒)
15、action.release(on_element=None)：在元素上释放按住的鼠标按钮
16、action.send_keys(*keys_to_send)：发送某个键到当前焦点的元素
17、action.send_keys_to_element(element, *keys_to_send)：发送某个键到指定元素


"""

from selenium.webdriver import ActionChains

import time
from selenium import webdriver
dr = webdriver.Chrome()
dr.get(url="https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
dr.maximize_window()

dr.implicitly_wait(3)
action = ActionChains(driver=dr)
dr.switch_to.frame('iframeResult')
time.sleep(2)
source = dr.find_element_by_xpath('//div[@id="draggable"]')

#获取元素坐标
#{"x":100,"y":200}
loc = source.location
print("元素坐标：",loc)

#收集命令
action.drag_and_drop_by_offset(source=source,xoffset=loc["x"],yoffset=loc["y"]+50).perform()

#执行命令
# action.perform()



