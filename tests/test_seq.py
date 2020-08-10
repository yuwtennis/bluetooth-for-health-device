
from iotble.flow.omron_hbf228t import body_composition_monitor

def test_body_composition_monitor():

    res = True

    try:
        seq_body_composition_monitor()
    except Exception as err:
        print(err)
        res = False

    assert res
