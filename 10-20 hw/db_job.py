# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 17:39:20 2022

@author: AlenChang
"""

import pymysql

dbsetting = {
    "host":"127.0.0.1",
    "port":3306,
    "user":"root",
    "password":"12345678",
    "db":"jobs",
    "charset":"utf8"    
    }

conn = pymysql.connect(**dbsetting)
