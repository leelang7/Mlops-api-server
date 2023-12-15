from datetime import datetime
import pandas as pd
from pandas_datareader import data as pdr
import pickle
import json
import yfinance as yf
yf.pdr_override()

dic = dict()
start = datetime(2023,1,1)
end = datetime(2023,12,31)
filename = datetime.now().strftime("%Y%m%d_%H%m%S")

df = pdr.get_data_yahoo('005930.KS', start, end)
#print(df)
#pic = pd.to_pickle(df, filename + '.pickle')
#print(dic)
print(type(df))
pic = df.to_json()
with open('temp.txt', 'w') as f:
    f.write(pic)
