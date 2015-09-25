# encoding:utf-8
import datetime,time

#把datetime转成字符串
def datetime_toString(dt,strformat='%Y-%m-%d %H:%M:%S'):
    return dt.strftime(strformat)

#把字符串转成datetime
def string_toDatetime(string,strformat='%Y-%m-%d %H:%M:%S'):
    return datetime.datetime.strptime(string, strformat)

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return int(time.mktime(string_toDatetime(strTime).timetuple()))

#把时间戳转成字符串形式
def timestamp_toString(stamp,strformat='%Y-%m-%d %H:%M:%S'):
    return time.strftime(strformat, time.localtime(stamp))

#把datetime类型转 时间戳形式
def datetime_toTimestamp(dateTim):
    return int(time.mktime(dateTim.timetuple()))

#把datetime类型转 时间戳形式
def timestamp_toDatetime(stamp,strformat='%Y-%m-%d %H:%M:%S'):
    strTime = timestamp_toString(stamp,strformat)
    return string_toDatetime(strTime,strformat)