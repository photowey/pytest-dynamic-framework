# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file http_request_executor
# @description http_request_executor
# @author WcJun
# @date 2021/07/19
# ---------------------------------------------

import http
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from fake_useragent import UserAgent

from src.main.python.request.http_request import HttpRequest


class RequestExecutor(object):
    """
    Http Request Executor
    """

    def execute(self, request: HttpRequest):
        """
        execute the http request.
        :param request: the HttpRequest
        :return: the HTTPResponse
        """
        method: str = request.method
        executor = self.switch(method)
        response: http.client.HTTPResponse = executor(request.url, request.headers)

        return response

    def switch(self, method: str):
        switch = {
            'get': self.handle_request_get,
            'post': self.handle_request_post,
            'put': self.handle_request_put,
            'patch': self.handle_request_patch,
            'delete': self.handle_request_delete
        }

        executor = switch[method]

        return executor

    @staticmethod
    def populate_headers() -> dict:
        """
        populate chrome headers \n
        :return:
        :rtype: dict
        """
        http_headers = {
            "User-Agent": UserAgent().chrome
        }

        return http_headers

    @staticmethod
    def populate_request(url: str, http_headers: dict) -> Request:
        """
        populate request \n
        :param url: URL
        :param http_headers: the headers
        :return: Request
        :rtype request
        """
        request = Request(url, headers=http_headers)

        return request

    @staticmethod
    def handle_request_get(url: str, http_headers: dict) -> http.client.HTTPResponse:
        """
        handle the get request \n
        :param url: the URL
        :param http_headers: the headers
        :return: the HTTPResponse
        """
        request = Request(url, headers=http_headers)
        response = urlopen(request)

        return response

    @staticmethod
    def handle_request_post(url: str, params: dict, http_headers: dict) -> http.client.HTTPResponse:
        """
        handle the post request \n
        :param url: the URL
        :param params: the params of Request
        :param http_headers: the headers
        :return: the HTTPResponse
        """
        form_data = urlencode(params).encode()
        request = Request(url, data=form_data, headers=http_headers)
        response = urlopen(request)

        return response

    @staticmethod
    def handle_request_put(url: str, params: dict, http_headers: dict) -> http.client.HTTPResponse:
        """
        handle the put request \n
        :param url: the URL
        :param params: the params of Request
        :param http_headers: the headers
        :return: the HTTPResponse
        """
        form_data = urlencode(params).encode()
        request = Request(url, data=form_data, headers=http_headers, method='put')
        response = urlopen(request)

        return response

    @staticmethod
    def handle_request_patch(url: str, params: dict, http_headers: dict) -> http.client.HTTPResponse:
        """
        handle the patch request \n
        :param url: the URL
        :param params: the params of Request
        :param http_headers: the headers
        :return: the HTTPResponse
        """
        form_data = urlencode(params).encode()
        request = Request(url, data=form_data, headers=http_headers, method='patch')
        response = urlopen(request)

        return response

    @staticmethod
    def handle_request_delete(url: str, params: dict, http_headers: dict) -> http.client.HTTPResponse:
        """
        handle the delete request \n
        :param url: the URL
        :param params: the params of Request
        :param http_headers: the headers
        :return: the HTTPResponse
        """
        form_data = urlencode(params).encode()
        request = Request(url, data=form_data, headers=http_headers, method='delete')
        response = urlopen(request)

        return response
