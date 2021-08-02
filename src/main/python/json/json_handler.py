# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file JSON
# @description JSON
# @author WcJun
# @date 2021/08/02
# ---------------------------------------------

import json


class JSON(object):
    """
    utilities function of JSON.
    """

    @staticmethod
    def toJSONString(dict_body: dict) -> str:
        """
        Serialize the dict object to a JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body)

    @staticmethod
    def toJSONStrings(dict_body: list) -> str:
        """
        Serialize the list object to a JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body)

    @staticmethod
    def toPrettyJSONString(dict_body: dict) -> str:
        """
          Serialize the dict object to a pretty JSON string.\n
          :param dict_body:
          :return:
          """
        return json.dumps(dict_body, sort_keys=True, indent=4)

    @staticmethod
    def toPrettyJSONStrings(dict_body: list) -> str:
        """
        Serialize the list object to a pretty JSON string.\n
        :param dict_body:
        :return:
        """
        return json.dumps(dict_body, sort_keys=True, indent=4)

    @staticmethod
    def parseObject(json_str: str) -> dict:
        """
        Deserialize the JSON string into a dict-object.\n
        :param json_str:
        :return:
        """
        return json.loads(json_str)

    @staticmethod
    def parseArray(json_str: str) -> list:
        """
        Deserialize the JSON string into a list-object.\n
        :param json_str:
        :return:
        """
        return json.loads(json_str)
