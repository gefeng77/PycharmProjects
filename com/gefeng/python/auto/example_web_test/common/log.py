# coding=utf-8
import logging
import time
import os


class Log(object):

    def get_logger(self):
        logger = logging.getLogger()
        logger.setLevel("INFO")

        # 定义日志文件的名称
        now = time.strftime("%Y%m%d %H%M%S")
        filename = os.path.dirname(os.getcwd()) + "/logs/" + now + ".log"

        # 创建一个handler，用于输出日志到文件
        fh = logging.FileHandler(filename)

        # 输出到log文件的日志级别
        fh.setLevel("DEBUG")

        # 定义日志输出格式
        formmater = logging.Formatter("%(asctime)s-%(name)s-%(filename)s-%(levelname)s-%(message)s")
        fh.setFormatter(formmater)

        logger.addHandler(fh)

        return logger


if __name__ == "__main__":
    logger = Log().get_logger()
    # 日志
    logger.debug("some debug message")
    logger.info("some info message")
    logger.warning("some warning message")
    logger.error("some error message")
    logger.critical("some critical message")



