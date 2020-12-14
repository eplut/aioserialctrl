from time import sleep

from aioserialctrl import SerialCtrl

port = "COM58"

with SerialCtrl(port) as serialctrl_obj:
    for _ in range(3):
        serialctrl_obj.write("AT\r\n".encode())
        ret = serialctrl_obj.read_until("OK\r\n".encode()).decode(errors="ignore")
        print(ret)