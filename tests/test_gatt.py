import sys
sys.path.append('../')

from src.gatt_tool_wrapper import GattToolWrapper
from src.const import *

def test_start_and_stop():
    res = True
    try:
        g = GattToolWrapper()
        g.start()
        g.stop()

    except Exception as err:
        print(err)
        res = False

    assert res

def test_connect():
    res = True
    try:
        g = GattToolWrapper()
        g.start()
        g.connect(DEV_UUID)
        g.stop()

    except Exception as err:
        print(err)
        res = False

    assert res
