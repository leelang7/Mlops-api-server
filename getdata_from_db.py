import os
import pymysql
import pandas as pd
import csv

def getdata_from_db(s, e):
    # Server connection 
    conn = pymysql.connect( 
        host='localhost',
        user='root',
        password='',
        db='samsung',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        # Create cursor
        with conn.cursor() as cursor:

            # Execute record select query
            select_query = f"select * from samsung.20231219 where Date between '{s}' and '{e}'"
            #select_query = 'select * from samsung.20231219'
            cursor.execute(select_query)
            result = cursor.fetchall() # list

            # Result -> DataFrame
            df = pd.DataFrame(result)
            # Print DataFrame
            #print(df)
            df.to_csv('data_from_db.csv', index=False)
    finally:
        # Close connection
        conn.close()

    return result # df에서 -> result로 수정함

def insert_data():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='', 
                           db='samsung', charset='utf8')
    curs = conn.cursor()
    conn.commit()
    ###
    files_Path = "C:\\Users\\admin\\LSC\\Mlops\\collect_files\\" # 파일들이 들어있는 폴더
    file_name_and_time_lst = []
    # 해당 경로에 있는 파일들의 생성시간을 함께 리스트로 넣어줌. 
    for f_name in os.listdir(f"{files_Path}"):
        written_time = os.path.getctime(f"{files_Path}{f_name}")
        file_name_and_time_lst.append((f_name, written_time))
    # 생성시간 역순으로 정렬하고, 
    sorted_file_lst = sorted(file_name_and_time_lst, key=lambda x: x[1], reverse=True)
    # 가장 앞에 이는 놈을 넣어준다.
    recent_file = sorted_file_lst[0]
    recent_file_name = recent_file[0]
    path = os.path.abspath(recent_file_name)
    print(path)
    f = open('C:\\Users\\admin\\LSC\\Mlops\\collect_files\\data_from_db.csv')
    csvReader = csv.reader(f)
    # Date,Open,High,Low,Close,Adj Close,Volume
    for row in csvReader:
        Date = (row[0])
        Open = (row[1])
        High = (row[2])
        Low = (row[3])
        Close = (row[4])
        AdjClose = (row[5])
        Volume = (row[6])
        sql = 'insert into samsung.20231219 (Date, Open, High, Low, Close, AdjClose, Volume) values (Date, Open, High, Low, Close, AdjClose, Volume)'
        curs.execute(sql)
    conn.commit()
    f.close()
    conn.close()
