# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file options
# @description options
# @author WcJun
# @date 2021/08/02
# ---------------------------------------------


class RequestOptions(object):

    def __init__(self, url, method='post', body=None, parameters=None, headers=None, ssl=False):
        """
        get-post-put-patch-delete
        :param url:
        :param method:
        """
        self.url = url
        self.method = method
        self.body = body

        self.headers = headers
        self.parameters = parameters
        self.ssl = ssl
