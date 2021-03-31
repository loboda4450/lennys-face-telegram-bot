import asyncio

from telethon import TelegramClient, events
import yaml


async def main(config):
	# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=config['log_level'])
	# logger = logging.getLogger(__name__)

	client = TelegramClient(**config['telethon_settings'])
	print("Starting")
	await client.start(bot_token=config['bot_token'])
	print("Started")

	@client.on(events.NewMessage())
	async def reply(event):
		await event.reply('( ͡° ͜ʖ ͡°)')

	@client.on(events.InlineQuery())
	async def reply_inline(event):
		if event.text:
			await event.answer(
				[event.builder.article(f'{event.text[:25]}... ( ͡° ͜ʖ ͡°)', text=f'{event.text} ( ͡° ͜ʖ ͡°)'),
				 event.builder.article(f'( ͡° ͜ʖ ͡°) {event.text[:25]}...', text=f'( ͡° ͜ʖ ͡°) {event.text}')])

		else:
			await event.answer([event.builder.article('( ͡° ͜ʖ ͡°)', text=f'( ͡° ͜ʖ ͡°)')])

	async with client:
		print("Good morning!")
		await client.run_until_disconnected()


if __name__ == '__main__':
	with open("config.yml", 'r') as f:
		config = yaml.safe_load(f)
		asyncio.get_event_loop().run_until_complete(main(config))
