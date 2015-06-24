#! /usr/bin/env python3
# -*- coding:UTF-8 -*-

from dbconn import db_cursor

def create_db():
    sqlstr = """
    DROP TABLE IF EXISTS student;

    CREATE TABLE IF NOT EXISTS student  (
    	stu_sn     TEXT,       --序号
    	stu_no     TEXT,       --学号
        sname      TEXT,        --姓名
        birthday   TEXT,      --出生日期
        sex        TEXT,     --性别
        sclass      TEXT,      --班级
        PRIMARY KEY(stu_no)
    );
    -- CREATE UNIQUE INDEX idx_student_no ON student(stu_no);

    CREATE SEQUENCE seq_stu_sn 
        START 10000 INCREMENT 1 OWNED BY student .stu_sn;

    """
    with db_cursor() as cur :
        cur.execute(sqlstr) # 执行SQL语句
    
def init_data():
    sqlstr = """
    DELETE FROM student;

    INSERT INTO student  (stu_sn, stu_no, sname,birthday,sex,sclass )  VALUES 
        (001, '1310650407',  '贾正旭', '19940228', '男','信息1304'),
        (002, '1310650406',  '覃理',  '19940812', '男','信息1304'),       
        (003, '1310650408',  '郭洪阳', '19940813', '男','信息1304'), 
        (004, '1310650420',  '刘佳',  '19940624', '女','信息1304'),        
        (005, '1310650227',  '郑然',  '19940324', '女','信息1302');        

    """
    with db_cursor() as cur : 
        cur.execute(sqlstr)    

if __name__ == '__main__':
    create_db()
    init_data()
    print('数据库已初始化完毕！')

