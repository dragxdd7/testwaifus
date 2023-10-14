from aiogram import Bot, Dispatcher, types
from motor.motor_asyncio import AsyncIOMotorClient
import re
import aiohttp
from aiogram import executor
import asyncio
from datetime import datetime

bot =Bot('6504156888:AAEg_xcxqSyYIbyCZnH6zJmwMNZm3DFTmJs')
dp = Dispatcher(bot)

client = AsyncIOMotorClient('mongodb+srv://shekharhatture:kUi2wj2wKxyUbbG1@cluster0.od4v7eo.mongodb.net/?retryWrites=true&w=majority')
db = client['anime_db']
collection = db['anime_collection']

CHANNEL_ID = -1001683394959
SUDO_USER_ID = [6404226395]
async def generate_id():
    for i in range(1, 10000):
        id = str(i).zfill(4)
        if not await collection.find_one({'_id': id}):
            return id
    return None

async def is_url_valid(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return response.status == 200
    except Exception:
        return False



@dp.message_handler(commands=['ping'])
async def ping(message: types.Message):
    start = datetime.now()
    sent_message = await message.reply("Pong!")
    end = datetime.now()
    elapsed_ms = (end - start).total_seconds() * 1000  # convert to milliseconds
    await sent_message.edit_text(f"Pong! Message speed: {elapsed_ms} milliseconds")

@dp.message_handler(commands=['upload'])
async def upload(message: types.Message):
    if int(message.from_user.id) in SUDO_USER_ID:
        try:
            _, img_url, anime_name, character_name = message.text.split(' ')
            anime_name = anime_name.replace('-', ' ')
            character_name = character_name.replace('-', ' ')
            # Validate the URL
            if not await is_url_valid(img_url):
                await message.reply("Invalid URL")
                return
            id = await generate_id()
            if id is None:
                await message.reply("Error: Database is full.")
                return
            doc = {
                '_id': id,
                'img_url': img_url,
                'anime_name': anime_name,
                'character_name': character_name
            }
            await collection.insert_one(doc)
            await message.reply("Successfully uploaded")
            # Send the information to the channel
            await bot.send_photo(
                CHANNEL_ID,
                img_url,
                caption=f"**ID:** {id}\n**Anime Name:** {anime_name}\n**Character Name:** {character_name}"
            )
        except Exception as e:
            await message.reply(f"Error: {str(e)}")
    else:
        await message.reply("You are not authorized to use this command.")

executor.start_polling(dp)
