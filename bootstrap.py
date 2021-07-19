# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file bootstrap
# @description bootstrap
# @author WcJun
# @date 2021/07/14
# ---------------------------------------------
import os

import pytest

python_path = 'src/main/python'


def clean_tmp_dir(target_path):
    """
    clean tmp dir
    """

    if os.path.exists(target_path):
        sub_files = os.listdir(target_path)
        for i in sub_files:
            sub_file = os.path.join(target_path, i)
            if os.path.isdir(sub_file):
                clean_tmp_dir(sub_file)
            else:
                print('remove the file:{}'.format(sub_file))
                os.remove(sub_file)


if __name__ == '__main__':
    # ---------------------------------------------
    # warning::it's dangerous
    clean_tmp_dir('./tmp')
    # ---------------------------------------------

    pytest.main()
    os.system('allure generate ./tmp -o ./report --clean')
