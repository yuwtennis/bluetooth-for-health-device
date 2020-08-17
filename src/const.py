"""List of constants.

Constants will be used widely accross classes and modules.

"""

import importlib

UUID_LIST = '{}/{}'.format(\
    importlib.import_module('iotble').__file__.replace('__init__.py', ''),\
    'data/omron_hbf228t_uuids.yaml')
HBF228T_DEV_ADDRESS = '28:FF:B2:BC:23:38'
