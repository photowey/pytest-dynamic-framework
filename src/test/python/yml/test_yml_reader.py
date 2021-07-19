# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_yml_reader
# @description test_yml_reader
# @author WcJun
# @date 2021/07/19
# ---------------------------------------------

import os

import pytest
import requests

from src.main.python.yml.yml_reader import YmlReader

yml_path = os.path.join(
    os.getcwd() + '{}src{}test{}resources{}test_yml_reader_yml.yml'.format(os.sep, os.sep, os.sep, os.sep))
reader = YmlReader(yml_path)
content = reader.read_yml()


class TestYmlReader:
    """
    test yml reader
    """

    @pytest.mark.parametrize('context', content)
    def test_yml_reader(self, context, logger):
        """
        do refresh access token
        """
        url = context['request']['url']
        parameters = context['request']['parameters']
        response = requests.get(url=url, params=parameters)
        logger.info('handle http request, the url:[{}]'.format(url))
        logger.info(
            'handle http request, the status_code:[{}],response body:[{}]'.format(response.status_code, response.text))
