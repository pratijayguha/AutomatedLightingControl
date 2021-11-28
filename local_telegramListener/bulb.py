import asyncio
from pywizlight import wizlight, PilotBuilder, discovery

async def async_getBulbAddress(ipRange):
    bulbs = await discovery.discover_lights(broadcast_space=ipRange)
    address = bulbs[0].__dict__['ip']
    return address


async def async_toggleBulb(light, status):
    if status == 'ON':
        await light.turn_on(PilotBuilder(brightness=255))
        return True
    elif status == 'OFF':
        await light.turn_off()
        return True
    else:
        return False

async def async_getBulbStatus(light):
    # Get the current color temperature, RGB values
    state = await light.updateState()
    status = state.get_state()
    return status


class bulb:
    def __init__(self, ipRange="192.168.1.255"):
        loop = asyncio.get_event_loop()
        self.address = loop.run_until_complete(async_getBulbAddress(ipRange))
        self.light = wizlight(self.address)

    def toggle(self, status):
        loop = asyncio.get_event_loop()
        status = loop.run_until_complete(async_toggleBulb(self.light, status))

    def getStatus(self):
        loop = asyncio.get_event_loop()
        status = loop.run_until_complete(async_getBulbStatus(self.light))
        return status
