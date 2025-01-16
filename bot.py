import logging
import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
from checkWord import checkWord
from transliterate import to_cyrillic, to_latin

API_TOKEN = '7400606942:AAHKFWU33exgRyptpn4DmP-5OuLk28TYB8c'

logging.basicConfig(level=logging.INFO)

# Bot va router obyektlarini yaratish
bot = Bot(token=API_TOKEN)
router = Router()

@router.message(F.text == "/start")  # Filtr sifatida F.text ishlatildi
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum, Xush kelibsiz! 😊😊😊")

@router.message(F.text == "/help")
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun biror-bir so'z yuboring.")

@router.message()
async def checkImlo(message: types.Message):
    words = message.text.strip().split()
    response = ""

    for word in words:
        result = checkWord(word)

        if result['available']:
            response += f"✅ {word.capitalize()}\n"
        else:
            response += f"❌ {word.capitalize()}\n"
            for text in result['matches']:
                response += f"✅ {text.capitalize()}\n"
        
    await message.answer(response)

async def main():
    # Dispatcher va routerni sozlash
    dp = Dispatcher()
    dp.include_router(router)  # Routerni dispatcherga qo‘shish

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
