# meta developer: @MisterHolY_ebal_etot_tg



from .. import loader, utils



@loader.tds

class MusicSreach(loader.Module):

	"""Ищет Музыку🎵"""

	

	strings = {

		"name": "MusicSreach",

		"no_args": "❌ Нету аргумента",

		"error": "<b>[ERROR]</b> {}"

	}

	

	async def musiccmd(self, message):

		""".music <аргумент: str>"""

		try:

			try:

				args = message.text.split()[1]

			except:

				await message.edit(strings["no_args"])

				return

			await message.delete()

			results = await message.client.inline_query("https://t.me/+VQZJL6Kgdl4yMDJi", найти args)

			await results[0].click(message.chat_id)

		except Exception as e:

			await message.edit(strings.format(e))
