import usb.core
import usb.util

class PerformaxDevice:
    def __init__(self):
        self.dev = self._find_device()
        if self.dev is None:
            raise ValueError('Device not found')
        self.dev.set_configuration()
        self._open()
        self.flush()

    def _find_device(self):
        return usb.core.find(idVendor=0x1589, idProduct=0xa101)

    def _ctrl_transfer(self, bRequest, wValue, wIndex, data):
        bmRequestType = 0x41
        ret = self.dev.ctrl_transfer(bmRequestType, bRequest, wValue, wIndex, data)
        return ret

    def _open(self):
        self._ctrl_transfer(0x02, 0x02, 0x00, [])

    def close(self):
        self._ctrl_transfer(0x02, 0x04, 0x00, [])

    def flush(self):
        self._ctrl_transfer(0x02, 0x01, 0x00, [])

    def send_command(self, cmd):
        self.dev.write(0x02, cmd, 100)
        response = self.dev.read(0x82, 1024, 100)
        sret = ''.join([chr(x) for x in response])
        return sret

    def __del__(self):
        self.close()
