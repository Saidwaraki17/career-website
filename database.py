from sqlalchemy import create_engine, text

import os
import pymysql

db_connection_str = "mysql+pymysql://imsl4hp5pvtsj2r6j1d0:pscale_pw_znfnpGGcpzcvB3w8x6hEO1uNf2SEZNktHKh1NyIjby8@aws.connect.psdb.cloud/career-website?charset=utf8mb4"
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
    result = conn.execute(
      text(f"SELECT * FROM jobs WHERE id = :val"),
      {"val": id}
    )
    rows = result.mappings().all()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])
    
    
