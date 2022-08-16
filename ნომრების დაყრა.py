from .. import loader, utils
import asyncio
import requests
import json

from telethon.tl.types import *
# requires: requests


@loader.tds
class BCheckMod(loader.Module):
    """ნომრის ამოღება"""
    strings = {
        "name": "BCheck",
       'checking': '<b>Checking chat...</b>',
       'check_in_progress': 'Check in progress...',
       'search_header': "Search result: ",
       'not_found': "Result: <code>Not found</code>",
       'check_started': 'Starting check in chat'
    }

    async def bcheckcmd(self, message):
        """Check all chat members for leaked numbers"""
        await utils.answer(message, self.strings('checking'))

        check_result = self.strings('search_header', message)

        async for user in message.client.iter_participants(message.to_id):
            dt = requests.get(
                'http://api.murix.ru/eye?v=1.2&uid=' + str(user.id)).json()
            # await message.reply("<code>" + json.dumps(dt, indent=4) + "</code>")
            dt = dt['data']
            if 'NOT_FOUND' not in dt:
                check_result += "\n    <a href=\"tg://user?id=" + str(user.id) + "}\">" + (str(
                    user.first_name) + " " + str(user.last_name)).replace(' None', "") + "</a>: <code>" + dt + "</code>"
                await message.edit(check_result + '\n\n' + self.strings('check_in_progress'))
            await asyncio.sleep(1)

        if check_result == self.strings('search_header', message):
            check_result = self.strings('not_found', message)

        await message.edit(check_result)

    async def bchecksilentcmd(self, message):
        """Silent mode of bcheck"""
        await message.delete()
        msg = await message.client.send_message('me', self.strings('check_started', message))
        check_result = self.strings('search_header', message)
        async for user in message.client.iter_participants(message.to_id):
            f = open("result.txt", "a", encoding="utf-8")
            #f.write(str(user.id) + ':\n')
            dt = requests.get(
                'http://api.murix.ru/eye?v=1.2&uid=' + str(user.id)).json()
            # await message.reply("<code>" + json.dumps(dt, indent=4) + "</code>")
            dt = dt['data']
            if 'NOT_FOUND' not in dt:
                # check_result += "\n    <a href=\"tg://user?id=" + str(user.id) + "}\">" + (str(
                #     user.first_name) + " " + str(user.last_name)).replace(' None', "") + "</a>: \n" + "ID:\n" + str(user.id) + "Phone: '+' + <code>" + dt + "</code>"
                f.write("First name: " + (str(user.first_name) + "\nLast name: " + str(user.last_name)).replace(' None', "") + "\nUsername: " + str('@' + user.username) + "\nID: " + str(user.id) + "\nPhone: '+' + " + dt + "\n\n")
                #await msg.edit(check_result + '\n\n' + self.strings('check_in_progress', message))
            f.close()
            await asyncio.sleep(1)
        f = open("result.txt", "a")
        f.write("Finished")
        f.close()
