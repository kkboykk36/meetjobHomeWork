# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 16:25:45 2022

@author: AlenChang
"""

'''
1.建立一個資料庫:jobs
2.在該資料庫建立2個table
    2-1.employee{id,name,sex,tel,assume(到職日)
    2-2.works{id,items,info,employeeid}

請使用python 執行sql語法
3.用python input將值(姓名,性別,電話,keyin日期)輸入至資料庫 employee table

4.用python input將值(工作項目,工作詳述,對應)輸入至資料庫 works table
員工id

5.使用者可依員工id來修改員工電話及性別

6.使用者可依編號查詢員工資料

7.使用者輸入員工資料查詢出工做詳述。
'''

import db_job
import datetime

while True:
    userChoose = input("請選擇欲執行的動作 1.新增員工資料 2.查詢員工資料 3.修改員工資料 4.離開\n")
    if userChoose == '1':
        insDataChoose = input("A.新增員工資料/B.新增工作內容\n").upper()
        if insDataChoose == 'A':
            empID = input("工號:\n")
            name = input("姓名:\n")
            sex = input("性別(F/M):\n").upper()
            tel = input("電話:\n")
            assume = datetime.date.today()
            sql = "insert into employee(employeeid,name,sex,tel,assume) values('{}','{}','{}','{}','{}')".format(empID,name,sex,tel,assume)
            cursor = db_job.conn.cursor()
            cursor.execute(sql)
            db_job.conn.commit()
            again = input("是否還要繼續?(Y/N)\n").upper()
            if again != 'Y':
                break
        else:
            item = input("職務:\n")
            info = input("職務內容:\n")
            empID = input("該職務人員(請輸入工號):\n")
            sql = "insert into works(item,info,employeeid) values('{}','{}','{}')".format(item,info,empID)
            cursor = db_job.conn.cursor()
            cursor.execute(sql)
            db_job.conn.commit()
            again = input("是否還要繼續?(Y/N)\n").upper()
            if again != 'Y':
                break
    elif userChoose == '2':
        qryDataChoose = input("A.查詢員工資料/B.查詢工作內容\n").upper()
        if qryDataChoose == 'A':
            empID = input("請輸入工號:\n")
            sql ="select * from employee where employeeid = '{}'".format(empID)
            cursor = db_job.conn.cursor()
            cursor.execute(sql)
            db_job.conn.commit()
            show = cursor.fetchall()
            print(show)
            again = input("是否還要繼續?(Y/N)\n").upper()
            if again != 'Y':
                break
        else:
            empID = input("請輸入工號:\n")
            sql ="select info from works where employeeid = '{}'".format(empID)
            cursor = db_job.conn.cursor()
            cursor.execute(sql)
            db_job.conn.commit()
            show = cursor.fetchall()
            print(show)
            again = input("是否還要繼續?(Y/N)\n").upper()
            if again != 'Y':
                break
    elif userChoose == '3':
        empID = input("請輸入工號:\n")
        sexMod = input("請修改性別:\n")
        telMod = input("請修改電話:\n")
        sql = "update employee set sex = '{}',tel = '{}' where employeeid = '{}'".format(sexMod,telMod,empID)
        cursor = db_job.conn.cursor()
        cursor.execute(sql)
        db_job.conn.commit()
        again = input("是否還要繼續?(Y/N)\n").upper()
        if again != 'Y':
            break


