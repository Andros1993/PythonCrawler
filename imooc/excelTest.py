import xlrd
import xlwt

file_name = xlwt.Workbook()
sheet = file_name.add_sheet("my_sheet")
file_name.save("D:/test.xls")

data = xlrd.open_workbook("D:/test.xls")
table = data.sheets()[0]