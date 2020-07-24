import pygatt

class Gatt:

    def __init__(self):
        self._adapter = pygatt.GATTToolBackend()

    def start(self):
        """Start module """
        self._adapter.start()

    def connect(self, dev_addr):
        """Connect to  device """
        self._device = self._adapter.connect(dev_addr)

    def stop(self):
        """Disconnect from any resources """
        self._adapter.stop()

    def find_handler_by_characertistic(self, uuid):
        pass

    def find_handler_by_descriptor(self, uuid):
        pass

    def char_read(self, handler, uuid):
        pass

    def write_cccd(self, handler, uuid):
        pass
