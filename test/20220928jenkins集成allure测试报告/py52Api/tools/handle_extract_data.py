"""
============================
Project: py52Api
Author:柠檬班-海励
Time:2022/8/24 21:46
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import json
from jsonpath import jsonpath


from tools.handle_attribute import HandleAttr

class HandleExtractData:
    def __init__(self):
        pass

    # extract_data = {"access_token":"$..access_token"}
    # response = {"access_token":"63fd01e4-0d47-4260-bf9c-af3801b515b3","token_type":"bearer","refresh_token":"c4127087-d024-454b-8c3b-05a6f73576aa","expires_in":1295999}
    def extract_data(self,response:dict,extract_data:str):
        if extract_data:
            extract_data = extract_data if isinstance(extract_data,dict) else json.loads(extract_data)
            for key,val in extract_data.items():
                #将token提取出来，
                value = jsonpath(response,val)[0]
                #并设置为类属性
                setattr(HandleAttr,key,value)
        else:
            print("excel中extract_data为空，不需要提取数据")


