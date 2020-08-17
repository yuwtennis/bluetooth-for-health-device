"""Class file."""

import binascii
from pygatt import GATTToolBackend

class FedoraClient(GATTToolBackend):
    """Wrapper to GATT tool.

    Inherits GATTToolBackend from pygatt modules.

    Attributes:
        None
    """

    def __init__(self) -> None:
        """Constructer for this class.

        Call super class constructer to initialize class variables.

        Args:
            self: Class object

        Returns:
            None

        Raises:
            None
        """
        super().__init__()

        self._device = None

    def connect(self, address: str, timeout=None, address_type=None, auto_reconnect=None) -> None:
        """Wrapper to connect function.

        Args:
            self: Class object
            address: device mac address
            timeout: None
            address_type: None
            auto_reconnect: None

        Returns:
            None

        Raises:
            None
        """
        self._device = super().connect(address, timeout, address_type, auto_reconnect)

    def str_read_char(self, uuid: str) -> str:
        """Wrapper for char_read and return handle as string

        Args:
            self: Class object
            uuid: UUID for characteristic

        Returns:
            handle: handle for characteristic

        Raises:
            None
        """
        return binascii.hexlify(self._device.char_read(uuid))
