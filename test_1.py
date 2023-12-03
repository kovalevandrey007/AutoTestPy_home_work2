import subprocess
import pytest


def checkout(cmd, text):
    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False

    # test1


def test_case1():
    assert checkout('cd /home/andy/test; 7z a ../out/arx1',
                    'Everything is Ok'), 'test1 FAIL'

    # test2


def test_case2():
    assert checkout('cd /home/andy/out; 7z e arx1.7z -o/home/andy/folder1 -y',
                    'Everything is Ok'), 'test2 FAIL'

    # test3


def test_case3():
    assert checkout('cd /home/andy/out; 7z t arx1.7z',
                    'Everything is Ok'), 'test3 FAIL'

    # test4


def test_case4():
    assert checkout('cd /home/andy/out; rm -rf -v arx1.7z',
                    "удалён 'arx1.7z'"), 'test4 FAIL'


def test_case5():
    assert checkout('cd /home/andy/ex; echo Hi!',
                    "Hi!"), 'test4 FAIL'
