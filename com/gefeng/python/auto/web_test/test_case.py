# coding=utf-8

import logging
import time
import os


class Logger(object):

    def __init__(self):
        # 创建一个logger，就是给log起的名字
        self.logger = logging.getLogger()
        self.logger.setLevel("INFO")

        # 创建一个handler，用于写入日志文件

        # 生成一个当前日期的日期字符串
        request_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        print(request_time)
        old_time = time.asctime()
        print(old_time)

        # os.getcwd()获取当前工作目录，os.path.dirname(os.getcwd())获取当前目录的上一级目录
        log_path = os.path.dirname(os.getcwd())+'/logs/'

        # print(os.getcwd())
        # print(log_path)

        # 拼成日志名称：路径+当前时间
        log_name = log_path + request_time + ".log"
        # 将日志信息输出到磁盘文件
        filehandler = logging.FileHandler(log_name)
        filehandler.setLevel("INFO")

        # 再定义一个handler，用于输出到控制台
        streamhandler = logging.StreamHandler
        streamhandler.setLevel(self, "INFO")

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        filehandler.setFormatter(formatter)
        streamhandler.setFormatter(self, formatter)

        # 给logger添加handler，即给logger添加不同的handler
        self.logger.addHandler(filehandler)
        self.logger.addHandler(streamhandler)

    def get_logger(self):
        return self.logger


if __name__ == "__main__":
    test_logger = Logger().get_logger()
    test_logger.debug("debug message")
    test_logger.info("info message")

