from sqlalchemy import create_engine, text

import pymysql

db_connection_str = "mysql+pymysql://a1qg70uvy4ubgeaqbjkh:pscale_pw_g25Ft6IF48KgqubxjbW86C5CfwAmUVsywZnHsLLGZvm@aws.connect.psdb.cloud/careerswebsite?charset=utf8mb4"
engine = create_engine(db_connection_str,
                      connect_args={
                        "ssl" :{
                        "ssl_ca":"/etc/ssl/cert.pem"
                        }
                      })

def load_jobs_from_db():
  with engine.connect() as conn:
   result = conn.execute(text("select * from jobs"))
   result_dict = []
   for row in result.all():
     result_dict.append(row._asdict())
   return result_dict

  