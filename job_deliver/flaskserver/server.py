# encoding:utf-8 
import sys, os
#sys.path.append('..')
sys.path.append('e:/workspace/job_deliver')
from flask import Flask, render_template, request, jsonify
from crawl.crawl import test_crawl, refresh_applied_jobs
from db.mongo import get_jobs
from db.mysql.mysql import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'



#@app.route('/crawl')
#def crawl():
#    test_crawl()
#    return 'crawl done'

#@app.route('/show_jobs/<int:n>')
#def show_jobs(n):
#    #jobs = get_jobs() # by mongodb
#    jobs = get_all_applied_jobs(n) # by mysql
#    return render_template('applied_jobs.html', jobs=jobs)

@app.route('/show_jobs')
def show_jobs():
    # sample http://localhost:5000/show_jobs?n=10
    n = request.args.get('n')
    try:
        n = int(n)
    except Exception, e:
        n = 30
    jobs = get_all_applied_jobs(n) # by mysql
    return render_template('applied_jobs.html', jobs=jobs)

@app.route('/recent_jobs')
def recent_jobs():
    # sample http://localhost:5000/show_jobs?n=10
    n = request.args.get('n')
    try:
        n = int(n)
    except Exception, e:
        n = 30
    if n < 0:
        n = 30
    #print n
    jobs = get_recent_apply(n) # by mysql
    return render_template('applied_jobs.html', jobs=jobs)

@app.route('/refresh_jobs')
def refresh_jobs():
    refresh_applied_jobs()
    return "refresh OK"

@app.route('/tmp')
def tmp():
    return render_template('tmp.html')

@app.route('/jobs/byjob')
def get_jobs():
    # sample http://localhost:5000/jobs/byjob?job=python
    job = request.args.get('job')
    jobs = get_by_job(job) # by mysql
    return jsonify(jobs)

@app.route('/jobs/bycompany')
def get_jobs_bycompany():
    # sample http://localhost:5000/jobs/bycompany?company=上海
    company = request.args.get('company')
    jobs = get_by_company(company) # by mysql
    return jsonify(jobs)

def runserver():
    app.debug = False
    app.run()

    
if __name__ == '__main__':

    pass