# 実行コマンド
# pytest test_pytest_conftest.py --os-name=mac -s

import os
import shutil

import pytest

import test_cal


class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = test_cal.Cal()
        cls.test_dir = '/tmp/test_dir'
        cls.test_file_name = 'test.txt'

    @classmethod
    def teardown_class(cls):
        if os.path.exists(cls.test_dir):
            shutil.rmtree(cls.test_dir)

    def test_save_no_dir(self):
        self.cal.save(self.test_dir, self.test_file_name)
        test_file_path = os.path.join(self.test_dir, self.test_file_name)
        print(f'test_file_path: {test_file_path}')
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double(self, request, csv_file):
        """ request,tmpdirなどの決まったfixture名+自分で作れる
        """
        print(csv_file)
        os_name = request.config.getoption('--os-name')
        print(os_name)
        if os_name == 'mac':
            print('ls')
        elif os_name == 'windows':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.test_file_name)
        test_file_path = os.path.join(tmpdir, self.test_file_name)
        print(f'test_file_path: {test_file_path}')
        assert os.path.exists(test_file_path) is True

    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            self.cal.add_num_and_double("1", 1)
