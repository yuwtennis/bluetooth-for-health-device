"""Defines communication flow for HB281."""

import logging
from time import sleep
from iotble.access import FedoraClient
from iotble import read_yaml
from iotble import HBF228T_DEV_ADDRESS, UUID_LIST

class HBF228T:

    @staticmethod
    def body_composition_monitor() -> None:
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
            gatt = GattToolWrapper()
            gatt.start()
            gatt.connect(HBF228T_DEV_ADDRESS)
    
            # Read characteristics for Device Information
            chars_to_read = [ v['char'] for k, v in data['di'].items() ]
            chars_to_read.extend([data['ws']['wsf']['char'],
                                  data['bc']['bcf']['char']])

            # Read characteristics
            for c in chars_to_read:
                logger_.info('Read char {}'.format().format(tr_read_char(c))
                sleep(1)

            descriptors = [ data['cts']['ct']['desc'],
                            data['bl']['bl']['desc'],
                            data['ucp']['ucp']['desc'],
                            data['dci']['dci']['desc'],
                            data['bc']['bcm']['desc'],
                            data['ws']['wm']['desc'],
                            data['pf']['pf']['desc']
            ]

            # Subscribe events
            for d in descriptors:
                logger_.info('Writing descriptrs...')
                gatt.subscribe(d)
                sleep(1)

            # Write characteristic
            # ToDo

        finally:
            gatt.stop()
