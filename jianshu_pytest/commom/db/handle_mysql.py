import logging
import time
from commom.db.read_mysql import Read_mysql
import pymysql


class DB(object):
    def __init__(self, config_file):
        self.read_mysql = Read_mysql(config_file)
        try:
            # 创建连接
            self.conn = pymysql.Connect(host=self.read_mysql.host, port=int(self.read_mysql.port), user=self.read_mysql.user, password=self.read_mysql.password, db=self.read_mysql.dbname, charset='utf8')
        except pymysql.err.OperationalError:
            logging.error('数据库密码错误')

    def select_data(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)

            self.close_conn()
        except pymysql.err.MySQLError:
            logging.error('sql 语句执行错误')
        else:
            return cur.fetchall()

    # 添加数据

    def insert_data(self, table_name, table_data):
        for key in table_data:
            table_data[key] = "'" + str(table_data[key]) + "'"

        key = ','.join(table_data.keys())
        values = ','.join(table_data.values())
        try:
            sql = "INSERT INTO " + table_name + " (" + key + ") " + "VALUES" + " (" + values + ") "
            with self.conn.cursor() as cur:
                cur.execute(sql)
            self.conn.commit()
            self.close_conn()

        except pymysql.err.ProgrammingError:
            logging.error("sql语句 语法 错误")
            self.conn.rollback()
        except pymysql.err.IntegrityError as e:
            logging.error("ID重复  msg : %s" % e)
        except pymysql.err.InternalError as e:
            logging.error("列名错误 msg : %s" % e)
        except Exception as e:
            logging.error(e)

    # 清除表中所有数据
    def clear_all(self, table_name):
        try:
            sql = "delete from " + table_name + ";"
            with self.conn.cursor() as cur:
                cur.execute("SET FOREIGN_KEY_CHECKS=0;")
                cur.execute(sql)
            self.conn.commit()
            self.close_conn() 
        except pymysql.err.MySQLError:
            self.conn.rollback()
        except Exception as e:
            self.conn.rollback()
            logging.error(e)

    def clears(self, sql):
        try:
            with self.conn.cursor() as cur:
                cur.execute(sql)
            self.conn.commit()
            self.close_conn()
        except Exception as e:
            logging.error("删除指定数据错误 msg : " % e)
            self.conn.rollback()

    # 关闭连接
    def close_conn(self):
        self.conn.close()


if __name__ == '__main__':
    # info_category
    table_data = {
        "create_time": "2019-01-19 14:22:14",
        "update_time": time.strftime("%Y-%m-%y %H:%M:%S", time.localtime()),
        "id": 13,
        "name": "test"
    }
    file = "./db_config.ini"
    db = DB(file)
    db.insert_data("info_category", table_data)
    # print(db.select_data("select * from info_category;"))


