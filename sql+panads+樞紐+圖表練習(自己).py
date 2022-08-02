# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:52:13 2022

@author: User
"""

"""
長條+圓餅
"""

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("Northwind.db")

sql = "select orderid,employeeid from Orders where orderdate like '%1996%' ;"
cursor1 = conn.execute(sql)
data = cursor1.fetchall()

ln = []
fn = []
emid = []

for row in data:
    sql2 = 'select lastname,firstname from employees where employeeid ="'+str(row[1])+'"'
    cursor2 = conn.execute(sql2)
    data2 = cursor2.fetchone()
    # print(data2[0])
    # print(data2[1])
    # print(row[1])
    ln.append(data2[0])
    fn.append(data2[1])
    emid.append(row[1])
    
# print(ln)
# print(fn)
# print(emid)
    
    
new = pd.DataFrame({'lastname':ln,'firstname':fn,'employeeid':emid})

print(new.pivot_table(index=['lastname','firstname',],values='employeeid',aggfunc='count'))

conn.close()


pic = new.pivot_table(index=['lastname','firstname',],values='employeeid',aggfunc='count')
#print(pic)
x = [10,20,30,40,50,60,70]
plt.bar(x,y=pic.employeeid,width=5,tick_label=pic.firstname,label='')

plt.legend()
plt.title = ('Sales Count')  #圖表標題
plt.xlabel('Sales')        #X軸名稱
plt.ylabel('Count')        #Y軸名稱
plt.show()