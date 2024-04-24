import sys
sys.path.append('.') # 경로 설정
from sqlalchemy import text
from project.common.maria_data_service import MariaDataService
import app_starter

maria_service = MariaDataService.instance()

def getdata_from_db(s, e):
    sql = f"select * from samsung.20231219 where Date between '{s}' and '{e}'"
    #print(sql, type(sql))
    test = maria_service.get(text(sql))
    print(len(test), test[0], type(test))
    return str(test)