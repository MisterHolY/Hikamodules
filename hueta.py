# meta developer: @fytva

from .. import loadr, utils

@loadertds

	"""Ищет модули с помощью бота @BampiOnBot"""
	
	strings = {
		"name": "Heta",
		"no_args": "❌ Нету аргумента",
		"error": "<b>[ERROR]</b> {}"
	}
	
	async def etacmd(self, message):
		""".nheta <args: str>"""
		try:
			try:
				args = message.text.split()[1]
			except:
				await message.edit(strings["no_args"])
				return
			await message.delete()
			results = await message.client.inline_query("@BampiOnBot", args)
			await results[0].click(message.chat_id)
		except Exception as e:
			await message.edit(strings.format(e))