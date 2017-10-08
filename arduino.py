import serial

class Arduino:
    """
    Creates arduino communication
    """
    def __init__(self, port="COM9"):
        self.ser = "0,0,0,0,0,0,0"
        self.last_data = [0,0,0,0,0,0,0]
        self.connect(port)

    def close(self):
        self.ser.close()

    def get_message(self):
        msg = self.ser.readline()
        return msg

    def get_data(self):
        msg = self.get_message()
        data = self.to_int_array(msg)
        self.last_data = data
        return data
        
    def send_message(self, msg):
        self.ser.write(msg)

    def connect(self, port):
        try:
            self.ser = serial.Serial(port, 9600, timeout=0.01)
        except SerialException:
            print "Error"
        
    def to_int_array(self, msg):
        try:
            a = msg.split(",")
            result = []
            for s in a:
                result.append(int(s))

            return result
        except ValueError:
            return self.last_data
        
        
