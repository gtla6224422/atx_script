#coding=utf8
from selenium import webdriver
import time
import MySQLdb

def connect():
    db = MySQLdb.connect("112.74.161.79",'root','C36^O6^dDaXo','job',charset = 'utf8')
    cursor = db.cursor()

    sql = 'select count(*) from job'

    try:
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            job_count = row[0]
            # 打印结果
            print "job_count=%s" % \
            (job_count)
    except:
            print "Error: unable to fecth data"

    return job_count
    # 关闭数据库连接
    db.close()

if __name__ == "__main__":
    connect()

