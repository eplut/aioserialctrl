import aioserialctrl.utils.ports

for serial_port_info in aioserialctrl.utils.ports.get_all():
    print(serial_port_info)