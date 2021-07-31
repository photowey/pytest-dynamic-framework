# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file encrypt_handler.py
# @description encrypt_handler
# @author WcJun
# @date 2021/07/22
# ---------------------------------------------


import os

import jpype


class EncryptHandler:

    def __init__(self):
        # ~\pytest-dynamic-framework\src\main\python\encrypt
        current_path = os.path.abspath(os.path.dirname(__file__))
        jar_path = os.path.abspath(os.path.join(current_path, '../../resources/encrypt/rsa-encryptor.jar'))
        # jdk version
        java_home = os.environ['JAVA_HOME']
        jpype.startJVM(
            '{}/bin/server/jvm.dll'.format(java_home),
            '-Djava.class.path={}'.format(jar_path),
            convertStrings=False
        )
        JClass = jpype.JClass('cn.org.opencharity.encrypt.Encryptor')
        self.instance = JClass()

    def encrypt(self, source) -> str:
        result = str(self.instance.encrypt(source))
        return result

    def decrypt(self, source) -> str:
        result = str(self.instance.decrypt(source))
        return result

    def shutdown(self):
        jpype.shutdownJVM()
