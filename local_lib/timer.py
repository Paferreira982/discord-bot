# CODE OBTAINED OVER THE INTERNET AND PERSONALIZATED BY PEDRO AUGUSTO
# Github: https://github.com/Paferreira982
# Description: Class necessary for doing intervals for assyncronous methods.

import asyncio

class Timer:
    def __init__(self, interval, first_immediately, client, callback):
        self._interval = interval
        self._first_immediately = first_immediately
        self._client = client
        self._callback = callback
        self._is_first_call = True
        self._ok = True
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        try:
            while self._ok:
                if not self._is_first_call or not self._first_immediately:
                    await asyncio.sleep(self._interval)
                await self._callback(self._client)
                self._is_first_call = False
        except Exception as ex:
            print(ex)

    def cancel(self):
        self._ok = False
        self._task.cancel()
