import logging
from logging.handlers import RotatingFileHandler


def log():
    logger = logging.getLogger(__name__)
    logging.basicConfig(level=logging.DEBUG)
    file_log_handler = RotatingFileHandler(filename='log.log', maxBytes=1024*1024*100, backupCount=10)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象 添加日志记录器
    logger.addHandler(file_log_handler)
    return logger


if __name__ == '__main__':
    log().debug('hhhhh')
    log().info('xixix')