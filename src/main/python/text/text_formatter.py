# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file text_formatter
# @description text_formatter
# @author WcJun
# @date 2021/08/02
# ---------------------------------------------


class Formatter(object):

    @staticmethod
    def text_format(text: str, *args) -> str:
        """
        format the str \n
        :param text: the origin str
        :param args: the args
        :return: the formatted str
        """
        return text.format(*args)
