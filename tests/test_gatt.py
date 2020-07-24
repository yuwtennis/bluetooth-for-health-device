import sys
sys.path.append('../')

from src.gatt import Gatt
from src.const import *

def test_start_and_stop():
    res = True
    try:
        g = Gatt()
        g.start()
        g.stop()

    except Exception as err:
        print(err)
        res = False

    assert res

def test_connect():
    res = True
    try:
        g = Gatt()
        g.start()
        g.connect(DEV_UUID)
        g.stop()

    except Exception as err:
        print(err)
        res = False

    assert res
