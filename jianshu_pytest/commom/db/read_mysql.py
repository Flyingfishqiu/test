import configparser


class Read_mysql(object):
    def __init__(self, config_file):
        cf = configparser.ConfigParser()
        cf.read(config_file)
        self.host = cf.get("mysqlconf", "host")
        self.port = cf.get("mysqlconf", "port")
        self.user = cf.get("mysqlconf", "user")
        self.password = cf.get("mysqlconf", "password")
        self.dbname = cf.get("mysqlconf", "dbname")