from jenkinsapi.jenkins import Jenkins
import sqlite3
from datetime import datetime

def get_job_details(cursor):
    print 'fetching job details...'
    # Refer Example #1 for definition of function 'get_server_instance'
    server = get_server_instance()
    now = datetime.now()
    for j in server.get_jobs():
        job_instance = server.get_job(j[0])
        cursor.execute('''INSERT INTO jenkins_jobs(name, status, timestamp)
                        VALUES(?,?,?)''', 
                        (job_instance.name, job_instance.is_running(), str(now)))

def get_server_instance():
    jenkins_url = 'http://invoizpaid_jenkins:8080'
    server = Jenkins(jenkins_url, username='kalada', password='kolops')
    return server

if __name__ == '__main__':
    conn = sqlite3.connect('invoizpaid/db.sqlite3')
    c = conn.cursor()
    c.execute('''
        DROP TABLE IF EXISTS jenkins_jobs
    ''')
    c.execute('''
        CREATE TABLE jenkins_jobs(id INTEGER PRIMARY KEY, name TEXT, status TEXT, timestamp TEXT)
    ''')

    get_job_details(c)
