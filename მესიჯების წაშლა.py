from .. import loader, utils

class DelmeMod(loader.Module):
    """წაშალე ყველა შენი გაგზავნილი მესიჯი"""
    strings = {'name': 'DelMe'}
    @loader.sudo
    async def delmecmd(self, message):
        """წაშალე შენგან გაგზავნილი მესიჯები"""
        chat = message.chat
        if chat:
            args = utils.get_args_raw(message)
            if args != str(message.chat.id+message.sender_id):
                await message.edit(f"<b>თუ შენ მართლა გინდა წაშალო წერილები,დაწერე ეს:</b>\n<code>.delme {message.chat.id+message.sender_id}</code>")
                return
            await delete(chat, message, True)
        else:
            await message.edit("<b>არ არის საჭირო პირად შეტყობინებაში ამის გამოყენება,ისედაც შეგიძლია წაშალო ჩატი!</b>")
    @loader.sudo
    async def delmenowcmd(self, message):
        """წაშალე შენგან გაგზავნილი მესიჯები,ყოველგვარი კითხვის გარეშე"""
        chat = message.chat
        if chat:
            await delete(chat, message, False)
        else:
            await message.edit("<b>არ არის საჭირო პირად შეტყობინებაში ამის გამოყენება,ისედაც შეგიძლია წაშალო ჩატი!</b>")

async def delete(chat, message, now):
    if now:
        all = (await message.client.get_messages(chat, from_user="me")).total
        await message.edit(f"<b>{all} მესიჯები წაიშალა!</b>")
    else: await message.delete()
    _ = not now
    async for msg in message.client.iter_messages(chat, from_user="me"):
        if _:
            await msg.delete()
        else:
            _ = "_"
    await message.delete() if now else "хули мусара хули мусара хули, едем так как ехали даже в хуй не дули"
