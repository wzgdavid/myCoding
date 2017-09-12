# encoding:utf-8 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy.orm import sessionmaker

from conf import engine
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Model(object):
    def save(self):
        session.add(self)
        session.commit()
        session.close()

    def delete(self):
        session.delete(self)
        session.commit()
        session.close()


class User(Base, Model):
    __tablename__ = 'users'
    _id = Column(Integer, primary_key=True)
    name = Column(String(20))
    fullname = Column(String(40))
    password = Column(String(40))
    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (
                            self.name, self.fullname, self.password)

    @classmethod
    def get_users_by_name(cls, name):
        return session.query(cls).filter_by(name=name).all()


class Applied_job(Base, Model):
        # 职位名  公司名  工作地点 薪资      申请日期     申请的简历      近两周申请      进度
        #(['job','company', 'place', 'salary', 'apply_date', 'resume_name', 'recent_apply', 'rate'])
    __tablename__ = 'applied_job'
    id = Column(Integer, primary_key=True)
    job = Column(String(100))
    company = Column(String(100))
    place = Column(String(30))
    salary = Column(String(30))
    apply_date = Column(String(30))
    resume_name = Column(String(50))
    recent_apply = Column(Integer)
    rate = Column(String(30))
    job_url = Column(String(100))
    #PrimaryKeyConstraint('job', 'company')
    #unique_job_comp = UniqueConstraint(job, company)
    UniqueConstraint(job, company)
    
    @classmethod
    def get_by_job(cls, job):
        return session.query(cls).filter_by(job=job).order_by(Applied_job.apply_date.desc()).all()

    @classmethod
    def get_by_company(cls, company):
        return session.query(cls).filter_by(company=company).order_by(Applied_job.apply_date.desc()).all()

    @classmethod
    def get_by_job_like(cls, job):
        if not job:
            return None
        like_str = '%{}%'.format(job)
        return session.query(cls).filter(Applied_job.job.like(like_str)).order_by(Applied_job.apply_date.desc()).all()

    @classmethod
    def get_by_company_like(cls, company):
        if not company:
            return None
        like_str = '%{}%'.format(company)
        return session.query(cls).filter(Applied_job.company.like(like_str)).order_by(Applied_job.apply_date.desc()).all()

    @classmethod
    def get_recent_apply(cls, n=30):
        rtn = session.query(Applied_job).order_by(Applied_job.apply_date.desc())[0:n]
        #print len(rtn), 'n 3'
        return rtn

def create_tables():
    Base.metadata.create_all(engine)

if __name__ == '__main__':

    #create_tables()
    ed_user = User(name='ji', fullname='Edf Jones', password='edspassword')
#
    #
    
    #User.add(ed_user)
    #session.delete(ed_user)
    #session.commit()
    #edd= User.get_users_by_name('edd')[0]
    #print edd
    #edd.fullname = 'www'
    #edd.save()
    #edd[1].delete()
    j = Applied_job.get_by_company_like('上海')
    print len(j)


    pass