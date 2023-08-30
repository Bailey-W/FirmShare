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
            print(f'Connecting to {self.port} at {self.baud} bps...')
        
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
    

    # Looks for message in format "||FS||UUID||"
    # Returns UUID or None if not found
    def identify(self):
        if self.debug:
            print("Identifying device...")
        timeout = 0
        messages = self.read_serial_messages()
        while not messages:
            sleep(1)
            messages = self.read_serial_messages()
            timeout += 1
            if timeout > 3:
                if self.debug:
                    print('')
                self.UUID = None
                return None
        for message in messages:
            if message.startswith("||"):
                parts = message[2:-2].split('||')
                if(parts[0] == "FS"):
                    self.UUID = parts[1]
                    return parts[1]
        return None

    # Reads all serial messages in the queue
    # Returns a list of all messages or None if there are no messages
    def read_serial_messages(self):
        # if there haven't been any messages, returns None
        if self.ser.in_waiting == 0:
            return None
        
        lines = []
        while self.ser.in_waiting > 0:
            lines.append(self.ser.readline().decode('utf-8').strip())

        if self.debug:
            print(lines)
        return lines

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

    def get_UUID(self):
        return self.UUID
    
    def get_port(self):
        return self.port
    
    def get_baud(self):
        return self.baud
    
    def get_connection_status(self):
        return self.connected

if __name__ == "__main__":
    conn = SerialConnector('/dev/ttyUSB0', 115200, False)
    conn.connect()
    print(conn.identify())
    for x in range(500):
        lines = conn.read_serial_messages()
        if lines:
            for line in lines:
                print(line)
        sleep(0.01)
    conn.disconnect()
    