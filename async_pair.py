import asyncio
import logging

from pylutron_caseta.pairing import async_pair

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(async_pair("192.168.106.62"))
