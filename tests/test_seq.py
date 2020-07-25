
from src.omron_seq_flow import seq_body_composition_monitor

def test_seq_body_composition_monitor():

    res = True

    try:
        seq_body_composition_monitor()
    except Exception as err:
        print(err)
        res = False

    assert res
