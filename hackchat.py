from .. import loader, utils
import logging
import asyncio
import time

logger = logging.getLogger(__name__)

@loader.tds
class HackChatMod(loader.Module):
	"""GroupHack your ass"""
	strings = {"name": "HackChat"}
	def __init__(self):
		self.name = self.strings["name"]
	def config_complete(self):
		pass
	async def hackchatcmd(self, message):
		"""HachChat your chat"""
		i = 0
		while i <= 99:
			await message.edit("<strong>Взлом чата выполнен на " + str(i) + "%</strong>")
			i += 1
			time.sleep(0.1)
		time.sleep(0.1)
		await message.edit("<strong>Чат успешно взломан! Его данные вы можете посмотреть в облаке Telegram.</strong>")
		return
