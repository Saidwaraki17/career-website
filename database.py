from sqlalchemy import create_engine, text

import os
import pymysql

db_connection_str = "mysql+pymysql://o0pez1w9w9xkpnzm1sli:pscale_pw_YEg6OkDwjiFuTs4bfmOi0KEFE8t375ppUNhSz3e8Bsc@aws.connect.psdb.cloud/career-website?charset=utf8mb4"
engine = create_engine(db_connection_str,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_dict = []
    for row in result.all():
      result_dict.append(row._asdict())
    return result_dict


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"SELECT * FROM jobs WHERE id = :val"),
                          {"val": id})
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
                 job_id=job_id, 
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])
