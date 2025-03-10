"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/26 20:47
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
from conf.setting import add_product_info
from tools.handle_attribute import HandleAttr
from tools.handle_path import image_dir
from tools.base_page import BasePage


import time
import pyautogui
from selenium.webdriver.common.by import By




class AddProduct:
    #1、点新增按钮
    add_button = {'loc': (By.XPATH, '//button[@class="el-button el-button--primary el-button--small"]/span[text()="新增"]'), 'page_action': '点新增'}
    #2、点商品图片,触发图片上传模态框
    product_image = {'loc': (By.XPATH, '//li[@class="el-upload-list__item"]/div[@tabindex="0" and @class = "el-upload el-upload--picture-card"]'), 'page_action': '点商品图片加号'}

    # 3、切换选项卡,点上传图片
    #switch_table = {'loc': (By.XPATH, '//div[@role="tablist"]/div[text()="{}"]'), 'page_action': '切换到'}

    # 4、点+图片上传，打开添加图片窗口，再从本地选择图片上传
    open_upload_window = {'loc': (By.XPATH, '//div[@class="upload-img-preview"]/div[@class="el-upload el-upload--picture-card"]'), 'page_action': '打开图片上传窗口'}

    # 5、确定上传图片
    upload_button = {'loc': (By.XPATH, '//span[text()="确定上传"]/parent::button'), 'page_action': '点确定上传'}

    # 6、选择图片，获取所有已上传的图片
    get_all_image = {'loc': (By.XPATH, '//div[@class="elx-main elx-img-list"]//img'), 'page_action': '获取所有上传的图片'}

    # 7、确认选择图片
    confirm_choice_image = {'loc': (By.XPATH, '//div[@class="el-badge item"]//span[text()="确 定"]'), 'page_action': '确认选择的图片'}

    # 8、产品分类(触发下拉菜单)
    product_class_list = {'loc': (By.XPATH, '//div[@class="el-cascader"]//input[@placeholder="请选择"]'), 'page_action': '点产品分类'}

    # 9 、产品下拉列表(参数化在方法里面)

    # 10、产品分组列表
    product_group_list = {'loc': (By.XPATH, '//label[text()="产品分组"]/following-sibling::div//input[@placeholder="请选择"]'), 'page_action': '点产品分组'}

    #11、退出产品分组选择
    product_group_exit = {'loc': (By.XPATH, '//label[text()="产品分组"]'), 'page_action': '点产品分组文字，退出产品分组选择'}

    #12、设置库存信息
    stock_setting = {'loc': (By.XPATH, '//tr//input[@class="el-input__inner"]'), 'page_action': '设置库存信息'}

    #13、设置物流信息
    freight_setting = {'loc': (By.XPATH, '//button[@type="button"]/preceding-sibling::div//input'), 'page_action': "运费设置"}

    #14、点包邮
    free_ship = {'loc': (By.XPATH, '//li/span[text()="包邮"]'), 'page_action': '点包邮'}

    #15、商品名称
    prod_info = {'loc': (By.XPATH, '//input[@placeholder="商品名称"]'), 'page_action': '商品名称'}

    #16、产品卖点
    prod_sell_option = {'loc': (By.XPATH, '//textarea[@placeholder="产品卖点"]'), 'page_action': '产品卖点'}

    #17、iframe切换
    iframe_path = {'loc': (By.XPATH, '//iframe'), 'page_action': '切换到产品详情iframe'}

    #18、产品详情body
    prod_description = {'loc': (By.XPATH, '//body[@id="tinymce"]'), 'page_action': '产品详情body框'}

    #19、确认添加产品
    add_confirm = {'loc': (By.XPATH, '//div[@class="el-form-item submit-product"]//span[text()="确 定"]/parent::button'), 'page_action': '添加产品确定按钮'}

    def __init__(self,driver):
        #元素操作
        self.base = BasePage(driver=driver)

    #点新增
    def click_add(self):
        self.base.find_element_and_click(locations=self.add_button["loc"],page_action=self.add_button["page_action"])

    #点商品图片,触发图片上传模态框
    def click_product_image(self):
        self.base.find_element_and_click(locations=self.product_image["loc"],page_action=self.product_image["page_action"])


    #切换到上传图片选项卡页面
    #切换到上传文件，切换到选择文件通用方法
    def switch_card(self,card_name):
        switch_table = {'loc': (By.XPATH, f'//div[@role="tablist"]/div[text()="{card_name}"]'), 'page_action': f'切换到{card_name}'}
        self.base.find_element_and_click(locations=switch_table["loc"],page_action=switch_table["page_action"])


    #点+图片上传，打开添加图片窗口，再从本地选择图片上传
    def upload_product_image(self):
        self.base.find_element_and_click(locations=self.open_upload_window["loc"], page_action=self.open_upload_window["page_action"])
        time.sleep(1)
        pyautogui.typewrite(image_dir)
        time.sleep(1)
        pyautogui.press(keys='ENTER',presses=3)

    #点击确认上传按钮(上传图片)
    def confirm_upload(self):
        self.base.find_element_and_click(locations=self.upload_button["loc"],page_action=self.upload_button["page_action"])


    #选择已经上传的图片
    def find_images_and_click(self):
        elements = self.base.find_more_element(locations=self.get_all_image["loc"],page_action=self.get_all_image["page_action"])
        elements[1].click()
        #确定选择该图片(必须选了图片之后确认按钮才可以点击，要等待元素课点击才能点)
        self.base.find_element_clickable_and_click(locations=self.confirm_choice_image["loc"],page_action=self.confirm_choice_image["page_action"])

    #产品下拉列表分类选择
    def product_list(self,class1="办公文具",class2="文具",class3="文件管理"):
        #触发下拉列表
        self.base.find_element_and_click(locations=self.product_class_list["loc"],page_action=self.product_class_list["page_action"])
        #选择下拉列表
        drop_down_list={"loc":(By.XPATH,f'//ul//span[text()="{class1}"]'),"page_action":f"一级菜单{class1}"}
        self.base.find_element_and_click(locations=drop_down_list["loc"],page_action=drop_down_list["page_action"])
        drop_down_list={"loc":(By.XPATH,f'//ul//span[text()="{class2}"]'),"page_action":f"一级菜单{class2}"}
        self.base.find_element_and_click(locations=drop_down_list["loc"],page_action=drop_down_list["page_action"])
        drop_down_list={"loc":(By.XPATH,f'//ul//span[text()="{class3}"]'),"page_action":f"一级菜单{class3}"}
        self.base.find_element_and_click(locations=drop_down_list["loc"],page_action=drop_down_list["page_action"])

    #选择产品分组下拉列表
    def product_group(self,name="每日上新"):
        #触发产品分组下拉列表
        self.base.find_element_and_click(locations=self.product_group_list["loc"],page_action=self.product_group_list["page_action"])
        #选择下拉列表 //span[text()="更多宝贝"]
        locs = {"loc":(By.XPATH,f'//span[text()="{name}"]'),"page_action":f"产品分组名称{name}"}
        self.base.find_element_and_click(locations=locs["loc"],page_action=locs["page_action"])
        #退出产品分组选择
        self.base.find_element_and_click(locations=self.product_group_exit["loc"],page_action=self.product_group_exit["page_action"])

    #设置库存信息(6个输入框)
    def stock_set(self):
        elements = self.base.find_more_element(locations=self.stock_setting["loc"],page_action=self.stock_setting["page_action"])
        #库存信息
        self.base.element_send_keys(element=elements[2],value=add_product_info["stock_list"][0])
        #商品编码
        self.base.element_send_keys(element=elements[3],value=add_product_info["stock_list"][1])


    #物流信息设置
    def freight_set(self):
        #触发下拉列表
        self.base.find_element_and_click(locations=self.freight_setting["loc"],page_action=self.freight_setting["page_action"])
        #点击包邮
        self.base.find_element_and_click(locations=self.free_ship["loc"],page_action=self.free_ship["page_action"])


    #设置产品信息
    def pro_info(self):
        #设置商品名称,设置为唯一，用于做产品断言
        product_name = f"py52测试专用产品{int(time.time()*1000)}"
        setattr(HandleAttr, "product_name",product_name)
        self.base.find_element_and_sendkeys(locations=self.prod_info["loc"], page_action=self.prod_info["page_action"],value=product_name)
        #设置产品卖点
        self.base.find_element_and_sendkeys(locations=self.prod_sell_option["loc"],page_action=self.prod_sell_option["page_action"],value=f"{product_name}卖点")

    #切换iframe
    def switch_to_iframe(self,in_dom=None):
        self.base.switch_iframe(locations=self.iframe_path["loc"],page_action=self.iframe_path["page_action"],in_dom=in_dom)


    #产品详情设置
    def product_descriptions(self):
        #切换iframe
        self.switch_to_iframe(in_dom=1)
        #设置产品详情body信息
        self.base.find_element_and_sendkeys(locations=self.prod_description["loc"],page_action=self.prod_description["page_action"],value="py52测试产品详情")
        #切换iframe
        self.base.switch_out_iframe()

    #确认添加产品
    def product_add_confirm(self):
        # 切换iframe
        self.base.find_element_and_click(locations=self.add_confirm["loc"],page_action=self.add_confirm["page_action"])

    #产品断言
    def assert_product(self):
        #获取新增产品的名称(唯一)
        product_name = getattr(HandleAttr,"product_name")
        #新增产品后的元素定位表达式
        product_path = {"loc":(By.XPATH,f'//span[text()="{product_name}"]'),"page_action":f"新增产品名称为{product_name}"}
        #如果添加的产品名称是唯一的，会返回3个元素对象
        elements = self.base.find_more_element(locations=product_path["loc"], page_action=product_path["page_action"],in_dom=1)
        assert len(elements) > 1
        print("添加产品断言成功")












