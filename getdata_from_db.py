import pymysql
import pandas as pd

def getdata_from_db(s, e):
    # Server connection 
    conn = pymysql.connect( 
        host='localhost',
        user='root',
        password='1436', 
        db='samsung',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        # Create cursor
        with conn.cursor() as cursor:

            # Execute record select query
            select_query = f"select * from samsung.20231216 where Date between '{s}' and '{e}'"
            #select_query = 'select * from samsung.20231216'
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