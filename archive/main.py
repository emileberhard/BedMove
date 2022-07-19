#!/usr/local/bin/python

from bleak import BleakClient
import asyncio
import time

address = "DFB18A2C-6BAB-439E-AF05-485FB4259B75"
MODEL_NBR_UUID = "99FA0002-338A-1024-8A49-009C0215F78A"


async def main(address):
    async with BleakClient(address) as client:
        for i in range(10):
            await client.write_gatt_char(MODEL_NBR_UUID, bytes.fromhex("0100"))
            time.sleep(0.5)


asyncio.run(main(address))
