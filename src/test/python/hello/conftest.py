# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file conftest.py
# @description conftest
# @author WcJun
# @date 2021/07/16
# ---------------------------------------------

import pytest

from src.main.python.logger.pytest_logger import PytestLogger


@pytest.fixture(
    scope='session',
    autouse=True
)
def logger():
    handler = PytestLogger()
    return handler
