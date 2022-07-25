#This Moduls Is Edited By Bloodyofc(Bloody Knife), tg:@bloodyofc
from .. import loader, utils
import logging
from requests import get
import io

@loader.tds
class WebShotMod(loader.Module):
 """ლინკზე გადასვლის შემდეგ სქრინის გადაღება"""
 strings = {
  "name": "WebShot"
 }
  
  
 @loader.sudo
 async def webshotcmd(self, message):
  """დაწერე .webshot და შემდეგ ლინკი, ასევე შეგიძლია დაურეფლიო ლინკს!<link>"""
  reply = None
  link = utils.get_args_raw(message)
  if not link:
   reply = await message.get_reply_message()
   if not reply:
    await message.delete()
    return
   link = reply.raw_text
  await message.edit("<b>📸დამელოდე,ვიღებ ფოტოს...</b>")
  url = "https://mini.s-shot.ru/1024x768/JPEG/1024/Z100/?{}"
  file = get(url.format(link))
  file = io.BytesIO(file.content)
  file.name = "webshot.png"
  file.seek(0)
  await message.client.send_file(message.to_id, file, reply_to=reply)
  await message.delete()
