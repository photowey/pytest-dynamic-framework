# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_excel_reader.py
# @description test_excel_reader
# @author WcJun
# @date 2021/07/31
# ---------------------------------------------

import os

from src.main.python.excel.excel_reader import ExcelReader


class TestExcelReader:

    def test_excel_reader(self):
        current_path = os.path.abspath(os.path.dirname(__file__))
        excel_path = os.path.abspath(os.path.join(current_path, '../../resources/test_excel.xlsx'))
        excel_reader = ExcelReader(excel_path)
        user_info = excel_reader.read_excel(sheet_name='test_excel')
        for item in user_info:
            assert len(item) == 4
            assert item[0] == '王大锤'
            assert item[1] == 2
            assert item[2] == 9528
            assert item[3] == ''
