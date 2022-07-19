#!/usr/local/bin/python

from bleak import BleakClient
import asyncio
import argparse

parser = argparse.ArgumentParser("bedmover.py")

parser.add_argument('direction', metavar='direction', type=str, help='which direction to move the bed')
parser.add_argument('amount', metavar='amount', type=str, help='how much to move the bed - \'alittle\', \'alot\' or \'fully\'')
args = parser.parse_args()
direction = args.direction
amount = args.amount

WALL_BED = "20A65F47-9746-2667-17AC-AC9F373C1E27"
WINDOW_BED = "DFB18A2C-6BAB-439E-AF05-485FB4259B75"
CONTROL_UUID = "99FA0002-338A-1024-8A49-009C0215F78A"

DIRECTIONS = {
    "legs_up": "0900",
    "legs_down": "0800",

    "back_up": "0B00",
    "back_down": "0A00",

    "up": "0100",
    "down": "0000"
}
AMOUNT = {
    'alittle': 3,
    'alot': 10,
    'fully': 40
}


async def main():
    wallmove = asyncio.create_task(movebed(WALL_BED))
    windowmove = asyncio.create_task(movebed(WINDOW_BED))
    await wallmove
    await windowmove


async def movebed(adress):
    async with BleakClient(adress) as client:
        for i in range(AMOUNT[amount]):
            await client.write_gatt_char(CONTROL_UUID, bytes.fromhex(DIRECTIONS[direction]))
            await asyncio.sleep(0.5)


asyncio.run(main())
