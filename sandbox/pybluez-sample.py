
# bluetooth low energy scan
#from bluetooth.ble import DiscoveryService
from gattlib import DiscoveryService
import time

if __name__ == '__main__':

    sleep = 10

    while True:

        service = DiscoveryService('hci0')
        devices = service.discover(1)

#        for address, name in devices.items():
#            print("name: {}, address: {}".format(name, address))
#
#            print(f'Sleeping {sleep} seconds.')
#            time.sleep(sleep)
