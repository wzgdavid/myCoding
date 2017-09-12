# encoding:utf-8 
import pymysql
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy import *
from sqlalchemy.orm import *
from models import session, Applied_job
#connstr = 'mysql+pymysql://wzg:123456Wzg@rm-uf6mrlj4j4v4to78so.mysql.rds.aliyuncs.com:3306/job_deliver?charset=utf8'
#engine = create_engine(connstr, echo=False) #True will turn on the logging  

'''
这里的方法给flask调用

这里调用models里的
'''

def get_all_applied_jobs(n=10):
    results = []
    query_rtn = session.query(Applied_job) if n <= 0 else session.query(Applied_job)[100:110] # fake
    for instance in query_rtn:
        results.append(__to_dict(instance))
    return results

def get_recent_apply(n=30):
    results = []
    query_rtn = Applied_job.get_recent_apply(n)
    for instance in query_rtn:
        results.append(__to_dict(instance))
    #print len(results), 'n2'
    return results

def get_by_job(job):
    jobs = Applied_job.get_by_job_like(job)
    dicted_jobs = []
    if jobs:
        for instance in jobs:
            dicted_jobs.append(__to_dict(instance))
    return dicted_jobs

def get_by_company(company):
    jobs = Applied_job.get_by_company_like(company)
    dicted_jobs = []
    if jobs:
        for instance in jobs:
            dicted_jobs.append(__to_dict(instance))
    return dicted_jobs

def __to_dict(applied_job):
    dicted_job = {}
    dicted_job['job'] = applied_job.job
    dicted_job['company'] = applied_job.company
    dicted_job['place'] = applied_job.place
    dicted_job['salary'] = applied_job.salary
    dicted_job['apply_date'] = applied_job.apply_date
    dicted_job['resume_name'] = applied_job.resume_name
    dicted_job['recent_apply'] = applied_job.recent_apply
    dicted_job['rate'] = None
    if applied_job.job_url is not None:
        dicted_job['job_url'] = applied_job.job_url
    else:
        dicted_job['job_url'] = '#'
    return dicted_job


if __name__ == '__main__':
    #ms = Mysql()
    #ms.create_table_applied_job()
    #m = MyORM()
    #m.test()
    #i = user.insert()
    #u = {'name':'tom', 'fullname':'tom smith'}
    #r1 = conn.execute(i, **u)
    #print len(get_all_applied_jobs(100))
    jobs  = get_by_job('python')

    for n in jobs:
        print n


