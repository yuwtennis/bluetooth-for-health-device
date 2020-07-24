"""Class file.
"""

from pygatt import GATTToolBackend
import binascii

class GattToolWrapper(GATTToolBackend):
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

    def start(self) -> None:
        """Wrapper to start function.

        https://github.com/peplin/pygatt/blob/8916795617b64d02877aeb115aa6371a2bd7e516/
            pygatt/backends/gatttool/gatttool.py#L244

        Args:
            self: Class object

        Returns:
            None

        Raises:
            None
        """
        super().start()

    def connect(self, dev_addr: str) -> None:
        """Wrapper to connect function.

        https://github.com/peplin/pygatt/blob/8916795617b64d02877aeb115aa6371a2bd7e516/
            pygatt/backends/gatttool/gatttool.py#L405

        Args:
            self: Class object
            dev_addr: device mac address

        Returns:
            None

        Raises:
            None
        """
        self._device = super().connect(dev_addr)

    def stop(self) -> None:
        """Wrapper to stop function.

        https://github.com/peplin/pygatt/blob/8916795617b64d02877aeb115aa6371a2bd7e516/
            pygatt/backends/gatttool/gatttool.py#L302

        Args:
            self: Class object
            dev_addr: device mac address

        Returns:
            None

        Raises:
            None
        """
        super().stop()

    def char_read(self, uuid: str) -> str:
        """Wrapper for char_read

        https://github.com/peplin/pygatt/blob/8916795617b64d02877aeb115aa6371a2bd7e516/
            pygatt/backends/gatttool/gatttool.py#L584

        Args:
            self: Class object
            uuid: UUID for characteristic

        Returns:
            handle: handle for characteristic

        Raises:
            None
        """
        return binascii.hexlify(self._device.char_read(uuid))

    def write_cccd(self, handle: str) -> None:
        """Wrapper for char_read

        https://github.com/peplin/pygatt/blob/8916795617b64d02877aeb115aa6371a2bd7e516/
            pygatt/backends/gatttool/gatttool.py#L553

        Args:
            self: Class object
            handle: handle

        Returns:
            handle: handle for characteristic

        Raises:
            NotificationTimeout
        """
        
        self._device.char_write_handle(handle)
