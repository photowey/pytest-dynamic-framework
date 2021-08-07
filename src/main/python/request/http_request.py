# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file http_request
# @description http_request
# @author WcJun
# @date 2021/07/19
# ---------------------------------------------

from src.main.python.request.options import RequestOptions


class HttpRequest:
    """
    Http Request
    """

    def __init__(self, options: RequestOptions):
        self.url = options.url
        self.method = options.method
        self.body = options.body

        self.headers = options.headers
        self.parameters = options.parameters
        self.ssl = options.ssl
        self.mock_enabled = options.mock_enabled
        self.mock_response = options.mock_response

    def populateUrlParameters(self) -> str:
        param_chain: [] = ['?']
        if type(self.parameters) == dict and len(self.parameters) > 0:
            for parameter_key in self.parameters.keys():
                single_param: [] = [parameter_key, '=', self.parameters[parameter_key], '&']
                param_chain.append(''.join(single_param))
        chain_str: str = ''.join(param_chain)

        return chain_str[:-1]
