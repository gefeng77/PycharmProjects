import logging
import time
import os


class LoggingMethod(object):

    def getlogger(self):
        logger = logging.getLogger()
        # Log等级总开关
        logger.setLevel(logging.INFO)

        # strftime()没有传入参数，则默认将localtime()当作参数
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        print(now)
        time_now = time.asctime()
        print(time_now)
        filename = os.path.dirname(os.path.abspath('.'))+'/log/'+now+'.log'

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(filename)

        # 输出到file的log等级的开关
        fh.setLevel(logging.DEBUG)

        # 定义handler的输出格式，每行日志输出，如上图，时间日期+执行类名称+日志级别+日志描述
        formatter = logging.Formatter("%(asctime)s-%(name)s-%(filename)s"
                          "[line:%(lineno)d]-%(levelname)s-%(message)s")
        fh.setFormatter(formatter)

        # 给logger添加Handler
        logger.addHandler(fh)

        return logger


if __name__ == "__main__":
    # 类名后需加上（），否则会报错
    # logger = LoggingMethod.getlogger()

    logger = LoggingMethod().getlogger()

    # 日志
    logger.debug("some debug message")
    logger.info("some info message")
    logger.warning("some warning message")
    logger.error("some error message")
    logger.critical("some critical message")
