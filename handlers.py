# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from dbconn import db_stulist

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/main.html")


class StudentListHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("pages/stu_list.html", students = dal_list_students())


def dal_list_students():
    data = []
    with db_cursor() as cur : # 取得操作数据的游标，记为cur
        s = """
        SELECT stu_sn, stu_no, sname, birthday,sex,sclass FROM student  ORDER BY stu_sn DESC
        """
        cur.execute(s)      
        for r in cur.fetchall():
            stu = dict(stu_sn=r[0], stu_no=r[1], sname=r[2], birthday=r[3],sex=r[4],sclass=r[5])
            data.append(stu)
    print(data)
    return data

