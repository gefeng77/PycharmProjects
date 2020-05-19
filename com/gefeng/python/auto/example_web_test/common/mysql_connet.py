# coding=utf-8
import pymysql


class Connect_SQL(object):
    def get_connect(self):
        connect = pymysql.connect("127.0.0.1", "root", "123456", "test_db", 3307, charset="utf-8")
        cursor = connect.cursor()
        try:
            sql = "select * from student where id = '%s'，% ('123')"
            cursor.execute(sql)
            data = cursor.fetchone()
            print(data)
        except:
            print("Cannot connect to DB")
        cursor.close()
        connect.close()


if __name__ == "__main__":
    connect_sql = Connect_SQL()
    connect_sql.get_connect()

