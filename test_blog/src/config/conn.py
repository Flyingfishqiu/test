import pymysql


class ConnMysql(object):
    def __init__(self,name,pwd):
        self.name = name
        self.pwd = pwd
        self.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='q123456', db='webdriver', charset='utf8')
        self.cursor =self.conn.cursor()

    # def conn_mysql(self):
    #     self.conn = pymysql.connect(host="127.0.0.1",port=3306, user=self.name, passwd=self.pwd, db='webdrver', charset='utf-8')
    #     self.cursor = self.conn.cursor()
        # return self.cursor

    def select(self,name):
        self.cursor.execute('select path FROM driver WHERE NAME="%s"'%name)
        return self.cursor.fetchone()

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    conn = ConnMysql("root", 'q123456')
    print(conn)
    print(conn.select('title'))