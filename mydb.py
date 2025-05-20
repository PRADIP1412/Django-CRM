# this is simple code for create database in mysql, we can do it in the workbench as well 

import mysql.connector

database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root'

)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("All Done.")