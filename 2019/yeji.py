#encoding utf-8
import xlrd
import os
rootdir='D:\\Users\\Administrator\\Desktop\\test'  # 放文件的目录
files = os.listdir(rootdir)
#shop_names = ['金创大厦','康桥万信酒店','川沙现代广场店','森兰商都','富海商务','高帆大厦','恒生万鹂','开文大厦','日月光','莲花科创园']

shop_names={
    '金创大厦': 4,     #  点名 ：行号
    '日月光': 5,
    '开文大厦': 6,
    '莲花': 7,
    '富海': 8,
    '浦东软件园-1': 9,
    '森兰商都': 10,
    '晓富金融': 11,
    '森兰国际': 12,
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
for filename in files:
    if filename == '张磊区组业绩2019.03.10.xlsx':  # 
        continue
    # 遍历每个店的业绩文件，把数据放在一个大的字典里  格式   {店1：[一串数据], 店2：[一串数据],.......}
    # 然后遍历这个字典，把数据填到区组业绩中
    for short_name in shop_names.keys():
        if short_name in filename:
        
            filepath = os.path.join(rootdir, filename)

    
            print(filepath)
            workbook = xlrd.open_workbook(filepath)

            sheet_name= '10'    # 表格名， 业绩中表示日期的日
            sheet = workbook.sheet_by_name(sheet_name)
            #print(sheet.cell(4,3))  # cell(行，列)   从0 开始
            #print(sheet.col_values(2))