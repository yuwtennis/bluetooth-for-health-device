"""Main method. """

from omron_seq_flow import *
import logging

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(name) %(levelname) %(message)s',
        level=logging.INFO)

    seq_body_composition_monitor()
