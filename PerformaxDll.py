import ctypes

# Define DLL file name and load DLL file
performax_dll = ctypes.cdll.LoadLibrary('./PerformaxCom.dll')

# Define function prototypes
performax_dll.fnPerformaxComGetNumDevices.restype = ctypes.c_bool
performax_dll.fnPerformaxComGetNumDevices.argtypes = [ctypes.POINTER(ctypes.c_ulong)]

performax_dll.fnPerformaxComGetProductString.restype = ctypes.c_bool
performax_dll.fnPerformaxComGetProductString.argtypes = [ctypes.c_ulong, ctypes.c_void_p, ctypes.c_ulong]

performax_dll.fnPerformaxComOpen.restype = ctypes.c_bool
performax_dll.fnPerformaxComOpen.argtypes = [ctypes.c_ulong, ctypes.POINTER(ctypes.c_ulonglong)]

performax_dll.fnPerformaxComClose.restype = ctypes.c_bool
performax_dll.fnPerformaxComClose.argtypes = [ctypes.c_ulonglong]

performax_dll.fnPerformaxComSetTimeouts.restype = ctypes.c_bool
performax_dll.fnPerformaxComSetTimeouts.argtypes = [ctypes.c_ulong, ctypes.c_ulong]

performax_dll.fnPerformaxComSendRecv.restype = ctypes.c_bool
performax_dll.fnPerformaxComSendRecv.argtypes = [ctypes.c_ulonglong, ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_void_p]

performax_dll.fnPerformaxComFlush.restype = ctypes.c_bool
performax_dll.fnPerformaxComFlush.argtypes = [ctypes.c_ulonglong]

class PerformaxDevice:
    def __init__(self, device_number=0):
        self.device_number = device_number
        self.handle = None
        self.open()
        self.flush()
        
    def open(self):
        handle = ctypes.c_ulonglong()
        if not performax_dll.fnPerformaxComOpen(self.device_number, ctypes.byref(handle)):
            raise Exception("Failed to open DMX-J-SA module")
        self.handle = handle
        
    def close(self):
        if not performax_dll.fnPerformaxComClose(self.handle):
            raise Exception("Failed to close DMX-J-SA module")
        self.handle = None
    
    def set_timeouts(self, read_timeout=1000, write_timeout=1000):
        if not performax_dll.fnPerformaxComSetTimeouts(read_timeout, write_timeout):
            raise Exception("Failed to set timeouts for DMX-J-SA module")
            
    def send_command(self, command, num_bytes_to_read=64):
        read_buffer = ctypes.create_string_buffer(num_bytes_to_read)
        write_buffer = bytes(command, 'ascii')
        if not performax_dll.fnPerformaxComSendRecv(self.handle, write_buffer, len(write_buffer), num_bytes_to_read, ctypes.byref(read_buffer)):
            raise Exception("Failed to send and receive data for DMX-J-SA module")
        return read_buffer.value.decode('ascii')
        
    def flush(self):
        if not performax_dll.fnPerformaxComFlush(self.handle):
            raise Exception("Failed to flush DMX-J-SA module buffer")
        
    @staticmethod
    def get_num_devices():
        num_devices = ctypes.c_ulong()
        if not performax_dll.fnPerformaxComGetNumDevices(ctypes.byref(num_devices)):
            raise Exception("Failed to get number of DMX-J-SA devices")
        return num_devices.value
    
    @staticmethod
    def get_product_string(device_number, options=0):
        buffer = ctypes.create_string_buffer(256)
        if not performax_dll.fnPerformaxComGetProductString(device_number, ctypes.byref(buffer), options):
            raise Exception("Failed to get product string for DMX-JSA device")
        return buffer.value.decode('ascii')
