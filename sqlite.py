# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 13:49:15 2018

@author: pkuntal
"""

import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)


create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY,name text, price real)" #real is double
cursor.execute(create_table)

connection.commit()
connection.close()




##create_table = "CREATE TABLE users__ (id int, username text, password text)"
##cursor.execute(create_table)
#
#user = (1, 'pooja', 'amd@123')
#insert_query = "INSERT INTO users__ VALUES (?,?,?)"
#cursor.execute(insert_query, user)
#
#users = [(2, 'pooja', 'amd@123'), (3, 'anand', 'amd@123')]
#cursor.executemany(insert_query, users)
#
#select = "SELECT * FROM users__"
#for row in cursor.execute(select):
#    print(row)