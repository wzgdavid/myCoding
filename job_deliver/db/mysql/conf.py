from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import *
from sqlalchemy.orm import *

connstr = 'mysql+pymysql://wzg:123456Wzg@rm-uf6mrlj4j4v4to78so.mysql.rds.aliyuncs.com:3306/job_deliver?charset=utf8'
engine = create_engine(connstr, echo=False) #True will turn on the logging  