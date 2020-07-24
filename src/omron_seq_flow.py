"""Defines communication flow for HB281."""

from gatt_tool_wrapper import GattToolWrapper
from util import *
from const import *
import logging

def seq_body_composition_monitor() -> None:
    """Runs flow for BCM

    Runs workflow for  Bluetooth standard protocol for Body Composition Monitor

    Args:
        None

    Returns:
        None

    Raises:
        None
    """
    logger_ = logging.getLogger(__name__)
    logger_.info('Start sequence flow.')

    try:
        # Read uuid list
        data = read_yaml(UUID_LIST)

        # Init Device
        g = GattToolWrapper()
        g.start()
        g.connect(DEV_UUID)

        # Read characteristics for Device Information
        for k,v in data['di'].items():
            logging.info(MSG_FORMAT_1.format(k,v['uuid'],g.read_char_as_str(v['uuid'])))

        # Read characteristics for Weight scale feature
        logger_.info(MSG_FORMAT_1.format('wsf',data['ws']['wsf']['uuid'],
            g.read_char_as_str(data['ws']['wsf']['uuid'])))

        # Read characteristics for Weight scale feature
        logger_.info(MSG_FORMAT_1.format('bc',data['bc']['bcf']['uuid'],
            g.read_char_as_str(data['bc']['bcf']['uuid'])))
    finally:
        g.stop()

