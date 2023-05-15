from sqlalchemy import create_engine, text
import os
import pymysql

db_connection_str = "mysql+pymysql://j8du6hiitogvd40eaaz3:pscale_pw_CKtIg2NZC2Vrf3wWuhbmodjMsGDd5CvcTUklXkVDvBy@aws.connect.psdb.cloud/career-website?charset=utf8mb4"
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
    
    
