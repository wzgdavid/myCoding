# encoding: utf-8

import csv, sys
import pyExcelerator as xlwr

filename = "/Users/myc/desktop/ios_check_user 2.csv"
reader = csv.reader(open(filename, "rb"))
book = xlwr.Workbook()  #创建工作簿
sheet = book.add_sheet('Sheet1')  #添加工作表
r = 0
try:
    for row in reader:
        #print row
        
        #for value in row:
        #    print value
        #    for c in range(len(row)):
        #        sheet.write(r, c)  #写入单元格
        #        print r, c ,value

        for c, value in enumerate(row):
            
            if c == 4:
                value = str(value)[:10]
            sheet.write(r, c, value)  #写入单元格
            print r, c ,value
        r += 1

except csv.Error, e:
    sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))

book.save('/Users/myc/Desktop/aa3')