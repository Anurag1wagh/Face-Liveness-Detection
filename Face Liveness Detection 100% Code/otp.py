# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 18:39:56 2021

@author: srcdo
"""

import math, random
import sqlite3
# for nuemeric OTP only

corpus= "0123456789"  

size = 4              # user may change this value

generate_OTP = ""
length = len(corpus)
for i in range(size) :
 generate_OTP+= corpus[math.floor(random.random() * length)]
print(generate_OTP)
my_conn = sqlite3.connect('face.db')
r_set=my_conn.execute("insert into face.credit(otp)values(?)where" + generate_OTP );