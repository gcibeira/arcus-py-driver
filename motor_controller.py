from DMXJSAModule import DMXJSAModule
import time

dmx = DMXJSAModule()


try:
    print(f"found devices: {dmx.get_num_devices()}")
    print(f"Device name: {dmx.get_product_string(0)}")
    dmx.open()
    dmx.flush()
    cmd = None
    while cmd != "END":
        cmd = input()
        print(dmx.send_command(cmd))
    dmx.close()
    
except:
    print("Error. Device not found")
