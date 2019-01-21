import os
import logbook
from logbook import Logger, TimedRotatingFileHandler
from logbook.more import ColorizedStderrHandler


def log_formatter(record, handler):
    log = "{dt}  {level}  {filename}  {func_name}  {lineno}  {msg}".format(
        dt=record.time,
        level=record.level_name,
        filename=os.path.split(record.filename)[-1],
        func_name=record.func_name,
        lineno=record.lineno,
        msg=record.message,
    )
    return log


def print_handler():
    # 日志路径，在主工程下生成log目录

    Log_Dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log')
    if not os.path.exists(Log_Dir):
        os.makedirs(Log_Dir)
    # 打印到屏幕句柄
    user_std_handler = ColorizedStderrHandler(bubble=True)
    user_std_handler.formatter = log_formatter
    # 打印到文件句柄
    file_handler = TimedRotatingFileHandler(os.path.join(Log_Dir, "%s.log" % "test_log"), date_format="%Y%m%d", bubble=True)
    file_handler.formatter = log_formatter
    return user_std_handler, file_handler


# 用户代码logger日志
def init_logger():
    user_log = Logger("user_log")
    user_std_handler, file_handler = print_handler()
    logbook.set_datetime_format("local")
    user_log.handlers = []
    user_log.handlers.append(user_std_handler)
    user_log.handlers.append(file_handler)
    return user_log


# 初始化日志系统（被默认调用）
user_log = init_logger()


def test():
    user_log.info("my test.")


if __name__ == "__main__":
    test()
