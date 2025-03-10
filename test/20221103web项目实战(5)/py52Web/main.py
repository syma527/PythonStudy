"""
============================
Project: py52Web
Author:柠檬班-海励
Time:2022/10/24 20:17
E-mail:2227092769@qq.com
Company:湖南零檬信息技术有限公司
Site: http://www.lemonban.com
Forum: http://testingpai.com 
============================
"""
import pytest

from tools.handle_path import allurefile_dir


# pytest.main(["-sv","test_cases/test_add_product.py","--clear-alluredir",])

pytest.main(["-sv","test_cases/test_add_product.py","--clean-alluredir","--alluredir=reports/allurefile"])












