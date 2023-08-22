import serial
from time import sleep

class SerialConnector:
    def __init__(self, port, baud=115200, debug=False):
        self.port = port
        self.baud = baud
        self.debug = debug
        self.connected = False

    # Connects to the previously specified port at the given baud rate
    # returns true if the connection is successful, or false if it is not
    def connect(self):
        if self.debug:
            print('Connecting to', self.port, 'at', self.baud, 'bps...')
        
        # Tries to connect to the serial port
        try:
            # Defines the connection parameters for the serial connection
            self.ser = serial.Serial(self.port, self.baud, timeout=1)
            # Checks to make sure that the name of the connected port is as expected
            if self.ser.name == self.port:
                self.connected = True
                if self.debug:
                    print("Connected to ", self.ser.name)
        except:
            self.connected = False
            if self.debug:
                print("Failed to connect to serial port")

        return self.connected
    
    # Disconnects from the serial port, only if previously connected
    def disconnect(self):
        if self.connected:
            if self.debug:
                print("Disconnecting...")
            self.ser.close()
            self.connected = False
        else:
            if self.debug:
                print("Unable to disconnect. Never connected.")


    # Updates the port value of the object
    # expects: port, a COM port of the computer
    def set_port(self, port):
        if self.connected:
            self.disconnect()
        self.port = port

    # Updates the baud rate
    # expects: baud, integer containing the new baud rate
    def set_baud(self, baud):
        if self.connected:
            self.disconnect()
        self.baud = baud

if __name__ == "__main__":
    conn = SerialConnector('/dev/ttyUSB0', 115200, True)
    print(conn.connect())
    conn.disconnect()
    