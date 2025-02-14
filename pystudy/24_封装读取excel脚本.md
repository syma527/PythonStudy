```
excel 封装  掌握


"""
from pprint import pprint
from openpyxl import load_workbook
class HandleExcel:
    def __init__(self,file_name,sheet_name):
        #创建表对象
        self.wb = load_workbook(filename=file_name)
        #创建sheet对象
        self.sheet_obj = self.wb[sheet_name]

    def get_cases(self):
        case_list = []
        cases = list(self.sheet_obj.iter_rows(values_only=True))
        title = cases[0] #获取表头
        values = cases[1:] #获取表数据
        for case in values:
            case_dict = dict(list(zip(title,case))) #将表数据和表头进行打包，变成dict
            case_list.append(case_dict) #将每一个测试用例加到list当中，集中返回
        self.close_file()
        return case_list

    def close_file(self):
        self.wb.close()

if __name__ == '__main__':
    cl = HandleExcel(file_name="cases.xlsx",sheet_name="Sheet1")
    result = cl.get_cases()
    pprint(result)
```

一、写excel文件【了解】

注意：写excel文件的时候要关闭excel，否则会报错

1、写单元格（覆盖）

sheet_obj["A1"] = "py52"

sheet_obj.cell(row=1,column=2,value="test_value")

2、追加写单元格（不会覆盖原有数据）

在excel最后行加入数据

可迭代对象的每个元素会占一个单元格，一个可迭代对象的数据占一行，不会换行

接收可迭代对象： list，tuple，dict，生成器

sheet_obj.append([1,2,3,4,5])

test_dict = {"A":"test1","B":"test2"}

```
from openpyxl import load_workbook
wb = load_workbook(filename="cases.xlsx")
sheet_obj = wb["Sheet1"]
# 追加写入（不覆盖数据）
#接收可迭代对象：list,tuple,dict,生成器
test_dict = [1,2,3,4,5]
test_dict = {"A":"test1","B":"test2"}
sheet_obj.append(test_dict)

wb.save("cases.xlsx")
#print(sheet_obj["B1"].value)
wb.close()
```

