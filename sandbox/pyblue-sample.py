
from bluepy import btle

if __name__ == '__main__':

   mac = '28:FF:B2:BC:23:38'

   b = btle.Peripheral()

   try:
       b.connect(mac)
       data = b.readCharacteristic(0x0811)

       print(data)

   finally:
       b.disconnect()
