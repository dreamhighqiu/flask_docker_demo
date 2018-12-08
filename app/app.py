#!/usr/bin/env python
# coding=UTF-8
"""
Desc：
Author：TavisD 
Time：2018-11-21 14:45
"""
import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return requests.get('https://api.apiopen.top/singlePoetry').text


@app.route("/users")
def get_users():
    import pymysql
    conn = pymysql.connect(host="docker_mysql_name", port=3306, user="root", passwd="123456", db="db_name_test", charset="utf8")
    cur = conn.cursor()
    sql = "select * from user"
    cur.execute(sql)
    rows = cur.fetchall()
    return str(rows)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
