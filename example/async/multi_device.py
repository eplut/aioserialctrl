import asyncio

from time import sleep

from aioserialctrl import AioSerialCtrl

port1 = "COM62"
port2 = "COM63"

async def test_connect(port, wait=3):
    with AioSerialCtrl(port) as aioserialctrl_obj:
        for _ in range(5):
            await aioserialctrl_obj.async_write("AT\r\n".encode())
            ret = await aioserialctrl_obj.async_read_until("OK\r\n".encode())
            print(f"{port}: {ret}")
            await asyncio.sleep(wait)


async def main():
    task1 = asyncio.create_task(test_connect(port1, 2))
    task2 = asyncio.create_task(test_connect(port2, 5))
    try:
        await task1
    except Exception as err:
        print(f"task1 error: {err}")
    try:
        await task2
    except Exception as err:
        print(f"task2 error: {err}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()