#from PerformaxDll import PerformaxDevice
from PerformaxUSB import PerformaxDevice

dmx = PerformaxDevice()

try:
    cmd = None
    while cmd != "END":
        cmd = input()
        print(dmx.send_command(cmd))
    dmx.close()
    
except:
    print("Error. Device not found")
