import pygatt
import util

if __name__ == '__name__'

    adapter = pygatt.GATTToolBackend()

    try:
        adapter.start()

        device = adapter.connect('28:FF:B2:BC:23:38')

        # Read Characteristic
        device.char_read()

    finally:
        adapter.stop()
