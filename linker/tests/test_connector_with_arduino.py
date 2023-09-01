###############
# Bailey Wimer
# 8/30/23
# test_connector_with_arduino.py
#
# Unit test cases for the SerialConnector object (WITH an arduino connected)
# NOTE: The arduino MUST have the corresponding test code loaded
###############

import unittest
import sys
import pathlib

# Automatically adds the 'linker' folder to the path for proper imports
path = pathlib.Path(__file__).parent.joinpath('../').resolve()
sys.path.append(str(path))

from serial_connector import SerialConnector

class TestSerialConnector(unittest.TestCase):

    # NOTE: this should be changed to match the correct port of the arduino
    PORT = '/dev/ttyUSB0'

    # Creates a SerialConnector object based on user input
    # The SerialConnector object will be used for the remainder of the tests
    def test_constructor_with_input(self):
        # port = input("Enter a port address for the arduino (i.e. /dev/ttyUSB0 or COM4)")
        print("Testing constructor...")
        self.conn = SerialConnector(self.PORT)
        self.assertEqual(self.conn.get_baud(), 115200, "Should be 115200 bps")
        self.assertEqual(self.conn.get_port(), self.PORT, "Port should match input")
        self.conn.disconnect()

    def test_connection(self):
        print("Testing connection...")
        self.conn = SerialConnector(self.PORT)
        res = self.conn.connect()
        self.assertEqual(res, True, 'Should be connected to serial port')
        self.assertEqual(self.conn.get_connection_status(), res, 'Connection Status should reflect result of connection')
        res = self.conn.disconnect()
        self.assertEqual(res, True)
        self.assertEqual(self.conn.get_connection_status(), False)

    def test_read_serial(self):
        print("Testing serial...")
        self.conn = SerialConnector(self.PORT)
        self.conn.connect()
        res = None
        while not res:
            res = self.conn.read_serial_messages()
        self.assertIn(res[0], ['||FS||AE012-01121||', 'This is a test'], "Message is incorrect")
        self.conn.disconnect()

    def test_identify(self):
        print("Testing identification...")
        self.conn = SerialConnector(self.PORT)
        res = self.conn.connect()
        res = self.conn.identify()
        self.assertEqual(res, 'AE012-01121')
        self.assertEqual(self.conn.get_UUID(), 'AE012-01121')
        self.conn.disconnect()

if __name__ == '__main__':
    unittest.main()
