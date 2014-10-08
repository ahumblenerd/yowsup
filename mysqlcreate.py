#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb

con = mdb.connect('localhost', 'root', 'toor', 'radio');

with con:
    cur = con.cursor()
    #cur.execute("DROP TABLE IF EXISTS Unreg")
    cur.execute("CREATE TABLE Unreg(Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,JID VARCHAR(30),regDate DATETIME,unregDate DATETIME,Channel INT)")    
    cur.execute("CREATE TABLE Registration(Id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,JID VARCHAR(30),Date DATETIME,Channel INT,UNIQUE KEY (JID))")
    cur.execute("CREATE TABLE Idcount(counted INT,id INT)")
    cur.execute("INSERT INTO Idcount VALUES (0,666)")
