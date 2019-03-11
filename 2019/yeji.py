#encoding utf-8
from copy import deepcopy
import xlrd, xlwt
import os
import numpy as np
import xlsxwriter
from xlutils.copy import copy 


rootdir='D:\\Users\\Administrator\\Desktop\\test'  # 放文件的目录
files = os.listdir(rootdir)
#shop_names = ['金创大厦','康桥万信酒店','川沙现代广场店','森兰商都','富海商务','高帆大厦','恒生万鹂','开文大厦','日月光','莲花科创园']
dest_file = '张磊区组业绩2019.03.10.xlsx'  # 需要统计的目标文件
sheet_name= '10'  # 表格名， 业绩中 表示日期的日
shop_names={
    '金创大厦': 2,     #  点名 ：行号
    '日月光': 3,
    '开文大厦': 4,
    '莲花': 5,
    '富海': 6,
    '浦东软件园-1':7,
    '森兰商都': 8,
    '晓富金融': 9,
    '森兰国际': 10,
    '浦东软件园-2': 13,
    '高帆大厦': 14,
    '复旦科技园': 15,
    '如意智慧酒店': 16,
    '外高桥店': 17,
    '张江集电港': 18,
    '传奇广场': 19,
    '光大安石': 20,
    '康桥万信': 22,
    '畅星大厦': 23,
    '中兴和泰': 24,
    '浦东机场': 25,
    '恒生万鹂': 26,
    '川沙现代广场': 27
}

dct = {}  # 把所有数据读入这个字典，然后把这个字典中的数据写到区组统计文件中
for filename in files:
    if filename == dest_file:  # 
        dest_file_path = os.path.join(rootdir, filename)
        continue
    # 遍历每个店的业绩文件，把数据放在一个大的字典里  格式   {店1：[一串数据], 店2：[一串数据],.......}
    # 然后遍历这个字典，把数据填到区组业绩中
    for short_name in shop_names.keys():
        #print(filename)
        if short_name in filename:
            
            filepath = os.path.join(rootdir, filename)

    
            #print(filepath)
            workbook = xlrd.open_workbook(filepath)

                
            tb = workbook.sheet_by_name(sheet_name)
            for i in range(1, 30):# 有些不一定写在第三行，所以要一行行检查，哪行有数据，记录哪行的数据
                data = [tb.cell(i,4).value, tb.cell(i,5).value, tb.cell(i,7).value,
                    tb.cell(i,9).value, tb.cell(i,10).value, tb.cell(i,11).value,
                    tb.cell(i,12).value, tb.cell(i,13).value, tb.cell(i,14).value]
                arr = np.array(data)
                #print(data, arr, arr.sum())
                lst = list(arr)
                #print(lst,type(lst[0]))
                if type(arr[0]) is np.float64: # 说明是数字，
                    #print(i,data)
                    dct[short_name] = deepcopy(data)
                    break

            #print(sheet.cell(3,2))  # cell(行，列)   从0 开始
            #print(sheet.col_values(2))


#print(dct)  # 虽然字典数据没错，但遍历重复了， 以后改



'''
-----------------------------
以上为读取数据， 这里开始写数据
------------------------------
'''
readbook = xlrd.open_workbook(dest_file_path)

writebook = copy(readbook) 
table = readbook.sheet_by_name(sheet_name)#通过名称获取

for k, v in dct.items():
    print(k, v)
    