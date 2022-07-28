#This Moduls Is Edited By Bloodyofc (Bloody Knife), tg:@bloodyofc
import re
from asyncio import sleep

from .. import loader, utils


@loader.tds
class ChatFuckerMod(loader.Module):
    """ფაქ ჩატ"""

    strings = {"name": "ფაქ ჩატ"}

    @loader.owner
    async def fccmd(self, message):
        """დაწერე .fc შემდეგ რაოდენობა, და დაწერე ტექსტი ან დაურეფლიე რაიმე ტექსტს!"""
        reply = await message.get_reply_message()
        repeat = 0
        text = ""
        if reply:
            if utils.get_args_raw(message):
                try:
                    if reply.text:
                        text = reply.text
                        repeat = int(utils.get_args_raw(message))
                    else:
                        await message.edit("ტექსტი არ არის!")
                        return
                except Exception:
                    await message.edit("<b>რაღაც შეგეშალა ბრატ!</b>")
                    return
            else:
                await message.edit("ჰმ,რაოდენობას არ უთითებ?")
                return
        elif utils.get_args_raw(message):
            try:
                repeat = int(utils.get_args_raw(message).split(" ")[0])
                text = re.split(r".[a-z-0-9]{1,} [0-9]{1,} ", message.text)[1]
            except Exception:
                await message.edit("<b>შეგეშალა რაღაც!</b>")
                return
        else:
            await message.edit("რაც შეეხება ტექსტს/დაურეფლიე ტექსტს?")
            return
        await message.delete()
        for _ in range(repeat):
            m = await message.client.send_message(message.to_id, text)
            await sleep(0.5)
            await m.delete()
            await sleep(0.1)
