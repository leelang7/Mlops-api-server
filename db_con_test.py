import pymysql
import pandas as pd
from sqlalchemy import create_engine

con = pymysql.connect(host='localhost', user='root', password='', 
                      db='samsung', charset='utf8')
query = 'select * from samsung.20231219'
df = pd.read_sql_query(query, con)
print(df)
print(len(df))

'''
pymysql.install_as_MySQLdb
engine = create_engine("mysql://user:password@host/db")
df.to_sql(name='new_performance_log', con=engine, if_exists='append', index=False) # append : table 존재시만 추가
'''