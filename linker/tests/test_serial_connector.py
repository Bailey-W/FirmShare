###############
# Bailey Wimer
# 8/30/23
# test_serial_connector.py
#
# Unit test cases for the SerialConnector object (without an arduino connected)
###############

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
        conn = SerialConnector('/dev/ttyUSB0', 9600, True)
        self.assertEqual(conn.get_baud(), 9600, "Should be 115200 bps")
        self.assertEqual(conn.get_port(), '/dev/ttyUSB0', "Port should be /dev/ttyUSB0")
        self.assertEqual(conn.get_connection_status(), False, "Should not start connected")

        conn2 = SerialConnector('/dev/ttyUSB1')
        self.assertEqual(conn2.get_baud(), 115200, "Should be 115200 bps")

    # Attempts to disconnect without first connecting
    def test_disconnect_without_connecting(self):
        conn = SerialConnector('/dev/ttyUSB0')
        self.assertEqual(conn.disconnect(), False, "Disconnect should return false, since it was never connected")

    # Creates a new SerialConnector with invalid port and attempts to connect
    def test_failed_connection(self):
        conn = SerialConnector("oops")
        self.assertEqual(conn.get_port(), "oops")
        self.assertEqual(conn.connect(), False, 'Should not be able to connect to "oops" port')
        self.assertEqual(conn.get_connection_status(), False, "Should not be connected")

    # Attempts to set a port with the constructor, then change it using the set_port
    def test_update_port(self):
        conn = SerialConnector('/dev/ttyUSB0')
        self.assertEqual(conn.get_port(), '/dev/ttyUSB0', "Port should be /dev/ttyUSB0")
        conn.set_port('COM4')
        self.assertEqual(conn.get_port(), 'COM4', "Port should have been changed to COM4")

    # Attempts to set a baud rate with the constructor, then change it using the set_baud
    def test_update_baud(self):
        conn = SerialConnector('COM4', 9600)
        self.assertEqual(conn.get_baud(), 9600, "Baud rate should be 9600 bps")
        conn.set_baud(38400)
        self.assertEqual(conn.get_baud(), 38400, "Baud rate should have changed to 38400 bps")

if __name__ == '__main__':
    unittest.main()
