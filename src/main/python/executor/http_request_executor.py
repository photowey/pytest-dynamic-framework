# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file http_request_executor
# @description http_request_executor
# @author WcJun
# @date 2021/07/19
# ---------------------------------------------

from urllib.parse import urlencode
from urllib.request import Request, urlopen

import requests
import requests_mock

from src.main.python.json.json_handler import JSON
from src.main.python.request.http_request import HttpRequest


def request_mock(request: HttpRequest):
    method: str = request.method
    remote_url: str = request.url
    mock_text: str = JSON.transferObject(request.mock_response)
    with requests_mock.Mocker() as mocker:
        if request.mock_enabled:
            if method == 'get':
                mocker.get(remote_url, text=mock_text)
                session = requests.Session()
                return session.get(remote_url, verify=request.ssl)
            elif method == 'post':
                mocker.post(remote_url, text=mock_text)
                session = requests.Session()
                return session.post(remote_url, verify=request.ssl)
            elif method == 'put':
                mocker.put(remote_url, text=mock_text)
                session = requests.Session()
                return session.put(remote_url, verify=request.ssl)
            elif method == 'patch':
                mocker.patch(remote_url, text=mock_text)
                session = requests.Session()
                return session.patch(remote_url, verify=request.ssl)
            elif method == 'delete':
                mocker.delete(remote_url, text=mock_text)
                session = requests.Session()
                return session.delete(remote_url, verify=request.ssl)


class RequestExecutor(object):

    def __init__(self):
        # do something
        pass

    """
    Http Request Executor
    """

    def execute(self, request: HttpRequest) -> requests.models.Response:
        """
        execute the http request.
        :param request: the HttpRequest
        :return: the HTTPResponse
        """
        method: str = request.method
        executor = self.switch(method)
        if request.mock_enabled:
            return request_mock(request)

        response: requests.models.Response = executor(request)

        return response

    def switch(self, method: str):
        switch_dict = {
            'get': self.request_get,
            'post': self.request_post,
            'put': self.request_put,
            'patch': self.request_patch,
            'delete': self.request_delete
        }

        executor = switch_dict[method]

        return executor

    def request_get(self, request: HttpRequest) -> requests.models.Response:
        """
        handle the get request \n
        :param request: the framework request object
        :return: the HTTPResponse
        """

        return requests.Session().get(request.url, params=request.parameters, verify=request.ssl)

    def request_post(self, request: HttpRequest) -> requests.models.Response:
        """
        handle the post request \n
        :param request: the framework request object
        :return: the HTTPResponse
        """

        return requests.Session().post(request.url, json=request.body, verify=request.ssl)

    def request_put(self, request: HttpRequest) -> requests.models.Response:
        """
        handle the put request \n
        :param request: the framework request object
        :return: the HTTPResponse
        """

        return requests.Session().put(request.url, json=request.body, verify=request.ssl)

    def request_patch(self, request: HttpRequest) -> requests.models.Response:
        """
        handle the patch request \n
        :param request: the framework request object
        :return: the HTTPResponse
        """

        return requests.Session().patch(request.url, json=request.body, verify=request.ssl)

    def request_delete(self, request: HttpRequest) -> requests.models.Response:
        """
        handle the delete request \n
        :param request: the framework request object
        :return: the HTTPResponse
        """

        return requests.Session().delete(request.url, verify=request.ssl)

    def _execute_request(self, request: HttpRequest, method: str) -> requests.models.Response:
        """
        handle the post request \n
        :param request: the framework request object
        :param method: the http method
        :return: the HTTPResponse
        """
        if request.body is not None:
            form_data = urlencode(request.body).encode()
            request = Request(request.url, data=form_data, headers=request.headers, method=method)
            response = urlopen(request)
        else:
            request = Request(request.url, headers=request.headers, method=method)
            response = urlopen(request)

        return response
