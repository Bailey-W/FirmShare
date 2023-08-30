import unittest
import sys
import pathlib

# Automatically adds the 'linker' folder to the path for proper imports
path = pathlib.Path(__file__).parent.joinpath('../').resolve()
sys.path.append(str(path))

from serial_connector import SerialConnector

class TestSerialConnector(unittest.TestCase):

    # Creates multiple objects using different constructor variations and tests them
    def test_constructor(self):
        conn = SerialConnector('/dev/ttyUSB0', 9600, False)
        self.assertEqual(conn.get_baud(), 9600, "Should be 115200 bps")
        self.assertEqual(conn.get_port(), '/dev/ttyUSB0', "Port should be /dev/ttyUSB0")

        conn2 = SerialConnector('/dev/ttyUSB1')
        self.assertEqual(conn2.get_baud(), 115200, "Should be 115200 bps")

    # Attempts to disconnect without first connecting
    def test_disconnect_without_connecting(self):
        conn = SerialConnector('/dev/ttyUSB0')
        self.assertEqual(conn.disconnect(), False, "Disconnect should return false, since it was never connected")

if __name__ == '__main__':
    unittest.main()
