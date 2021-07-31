# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file test_encrypt_handler.py.py
# @description test_encrypt_handler.py
# @author WcJun
# @date 2021/07/31
# ---------------------------------------------


from src.main.python.encrypt.encrypt_handler import EncryptHandler


class TestEncryptHandler:

    def test_encrypt_handler(self):
        handler = EncryptHandler()
        encrypt_result = handler.encrypt('123456')
        # RQDOkImMU2vg2m9EJbaDgDzmzofpcqD2HTWl0Awlcn62czLgmJYlkPeX+v2JYn3lsPb3j5S0wAh/HSzUy3ltgtsrZtwYdvU+Mnw0XahqCZ+iXyRdWUGnT45bR3XzKxtg+vGfq2m/kLBsYt0DSZ9K5/k0owMPLauRNJFeL8xQIcwjLK/sTCtti8TFskooJ2n5i7B/KXBddzyOKTPd09lDbzErAgNuCPuo6z+R2c/FYnmnSJ6MlXrGfTP5I9c9snb8v5yttw3duhSSZGBe9zSDsvgWLEjtLlgPpZN112+2K8STOyxlg0pPKY4tv2670NmgER6hCxYfP7FGFmiUP6aSEg==
        decrypt_result = handler.decrypt(encrypt_result)
        assert decrypt_result == '123456'
        handler.shutdown()
