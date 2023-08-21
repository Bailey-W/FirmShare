import serial
from time import sleep

class SerialConnector:
    def __init__(self, port, baud=115200, debug=False):
        self.port = port
        self.baud = baud
        self.debug = debug
        self.connected = False

    # Connects to the previously specified port at the given baud rate
    def connect(self):
        if self.debug:
            print('Connecting to', self.port, 'at', self.baud, 'bps...')
        self.ser = serial.Serial(self.port, self.baud, timeout=1)
        if self.ser.name == self.port:
            self.connected = True
        if self.debug:
            print("Connected to ", self.ser.name)
        return self.connected
    
    def disconnect(self):
        if self.connected:
            if self.debug:
                print("Disconnecting...")
            self.ser.close()
            self.connected = False

    def set_port(self, port):
        if self.connected:
            self.disconnect()
        self.port = port

    def set_baud(self, baud):
        if self.connected:
            self.disconnect()
        self.baud = baud
    
    


if __name__ == "__main__":
    conn = SerialConnector('/dev/ttyUSB0', 115200, True)
    conn.connect()
    sleep(5)
    conn.disconnect()
    