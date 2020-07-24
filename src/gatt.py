import pygatt

class Gatt:

    """Fetches rows from a Smalltable.
    """

    def __init__(self):
        self._adapter = pygatt.GATTToolBackend()

    """Fetches rows from a Smalltable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by table_handle.  String keys will be UTF-8 encoded.

    Args:
        table_handle: An open smalltable.Table instance.

    Returns:
        A dict mapping keys to the corresponding table row data

    Raises:
        IOError: An error occurred accessing the smalltable.
    """
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
