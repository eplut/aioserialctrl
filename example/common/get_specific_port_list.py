import aioserialctrl.utils.ports

for serial_port_info in aioserialctrl.utils.ports.grep("^Test"):
    print(serial_port_info)