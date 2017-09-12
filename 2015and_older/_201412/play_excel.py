# encoding: utf-8
import random
import xlrd
import pyExcelerator as xlwr

book = xlrd.open_workbook('/Users/myc/Desktop/aa.xlsx')
sheet = book.sheet_by_index(0)

# read
row = sheet.row(0)
cell = sheet.cell(0, 0).value
#print cell


# write

book = xlwr.Workbook()  #创建工作簿
sheet = book.add_sheet('Sheet1')  #添加工作表
sum = 200
for n in range(100):
    sum += random.randint(-10, 10)
    sheet.write(n, 0, sum)  #写入单元格   
book.save('/Users/myc/Desktop/aa2')
