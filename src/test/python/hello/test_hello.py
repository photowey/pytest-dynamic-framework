# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_hello
# @description test_hello
# @author WcJun
# @date 2021/07/14
# ---------------------------------------------


# ---------------------------------------------
# pytest 规范
# 1.模块名: 以 {@code test_} 开头 或者 以 {@code _test} 结尾
# 2.类型以 {@code Test} 开头
# 3.测试方法以: {@code test} 开头
# ---------------------------------------------

from src.main.python.logger.pytest_logger import PytestLogger


class TestHelloWorld:
    """
    test hello_world
    """

    def test_hello_world(self, logger):
        """
        test_hello_world
        :return:
        """
        logger.info('say \'HelloWorld\' from pytest-dynamic-framework!')
