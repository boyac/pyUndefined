# #!/usr/local/bin/python
# coding: utf-8

import pandas
import time
from datetime import datetime
import sqlite3

dfs = pandas.read_html('http://rate.bot.com.tw/xrt?Lang=zh-TW')
currency = dfs[0]

#選取需要的[row,column]
currency = currency.ix[:,0:5] 

#修改 column header
currency.columns = [u'幣別', u'現金匯率-本行買入', u'現金匯率-本行賣出', u'即期匯率-本行買入', u'即期匯率-本行賣出'] 
currency[u'幣別'] = currency[u'幣別'].str.extract('\((\w+)\)')
currency.to_excel('yen_rate.xlsx')
currency['Date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
currency['Date'] = pandas.to_datetime(currency['Date'])  #修改資料庫欄位類型
#currency.info()

#寫入 yen_rate 資料庫
with sqlite3.connect('/Users/boyac/mystuff/currency.sqlite') as db:
    currency.to_sql('yen_rate', con = db, if_exists='append')

#讀取 yen_rate 資料庫
with sqlite3.connect('/Users/boyac/mystuff/currency.sqlite') as db:
    df = pandas.read_sql_query('select * from yen_rate', con = db)
