import sys
sys.path.append('../src')

from gatt_tool_wrapper import GattToolWrapper
from const import DEV_ADDRESS

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
        g.connect(DEV_ADDRESS)
        g.stop()

    except Exception as err:
        print(err)
        res = False

    assert res

def test_char_read():
    res = True
    try:
        g = GattToolWrapper()
        g.start()
        g.connect(DEV_ADDRESS)

        # Read Model number string
        g.char_read_as_str('00002a24-0000-1000-8000-00805f9b34fb')
        g.stop()

    except Exception as err:
        print(err)
        res = False

    assert res

