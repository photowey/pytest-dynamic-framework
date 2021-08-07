# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_http_request
# @description test_http_request
# @author WcJun
# @date 2021/07/19
# ---------------------------------------------

import requests
from fake_useragent import UserAgent

from src.main.python.executor.http_request_executor import RequestExecutor
from src.main.python.request.http_request import HttpRequest
from src.main.python.request.options import RequestOptions

body = {'world': 'python'}
parameters = {'world': 'python'}
mock_response = {'method': 'mock', 'world': 'hello python'}

headers = {
    'User-Agent': UserAgent().chrome
}


def do_request(options: RequestOptions):
    request = HttpRequest(options)
    executor = RequestExecutor()
    response: requests.models.Response = executor.execute(request)

    assert response.status_code == 200


class TestRequestExecutor(object):

    def test_request_get(self):
        options = RequestOptions(
            url='http://192.168.2.172:10115/zcjfinance/hello/sayHello',
            method='get',
            parameters=parameters,
            headers=headers,
            ssl=False
        )
        # {"method":"get","name":"hello python"}
        do_request(options)

    def test_request_post(self):
        options = RequestOptions(
            url='http://192.168.2.172:10115/zcjfinance/hello/sayHello',
            method='post',
            body=body,
            headers=headers,
            ssl=False
        )
        # {"method":"post","name":"hello python"}
        do_request(options)

    def test_request_put(self):
        options = RequestOptions(
            url='http://192.168.2.172:10115/zcjfinance/hello/sayHello',
            method='put',
            body=body,
            headers=headers,
            ssl=False
        )
        # {"method":"put","name":"hello python"}
        do_request(options)

    def test_request_patch(self):
        options = RequestOptions(
            url='http://192.168.2.172:10115/zcjfinance/hello/sayHello',
            method='patch',
            body=body,
            headers=headers,
            ssl=False
        )
        # {"method":"patch","name":"hello python"}
        do_request(options)

    def test_request_delete(self):
        options = RequestOptions(
            url='http://192.168.2.172:10115/zcjfinance/hello/sayHello',
            method='delete',
            headers=headers,
            ssl=False
        )
        # {"method":"delete","name":"hello world"}
        do_request(options)

    def test_request_mock(self):
        options = RequestOptions(
            url='http://192.168.2.172:10115/zcjfinance/hello/mock',
            method='delete',
            headers=headers,
            ssl=False,
            mock_enabled=True,
            mock_response=mock_response
        )
        # {"method": "mock", "world": "hello python"}
        do_request(options)
