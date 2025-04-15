import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters.command import Command
import re


logging.basicConfig(level=logging.INFO, filename="bot.log",encoding="utf-8")
bot= Bot(token="use your key")
dp= Dispatcher()


@dp.message(Command(commands=["start"]))
async def start_proc(message:Message):
    user_name= message.from_user.full_name
    user_id= message.from_user.id
    text1= "Привет! Напиши свое полное Фио"
    logging.info(f"{user_name}{user_id} начал чат с ботом")#, filename="log_bot.log")
    await bot.send_message(chat_id=user_id, text=text1)


@dp.message()
async def transp_fio(message:Message):
    user_name= message.from_user.full_name
    user_id= message.from_user.id
    text_for_transp= message.text.strip()
    logging.info(f"{user_name}{user_id} отправил текст {text_for_transp}")#, filename="log_bot.log")
    result=[]
    letters= {"а":"a","б":"b","в":"v","г":"g","д":"d","е":"e","ё":"e","ж":"zh","з":"z","и":"i","й":"i","к":"k",
              "л":"l","м":"m","н":"n","о":"o","п":"p","р":"r","с":"s","т":"t","у":"u","ф":"f","х":"kh","ц":"ts",
              "ч":"ch","ш":"sh","щ":"shch","ы":"y","ъ":"ie","э":"e","ю":"iu","я":"ia"}
    pattern=r'^[А-ЯЁа-яё]+\s[А-ЯЁа-яё]+\s[А-ЯЁа-яё]+$'
    if not re.match(pattern,text_for_transp):
        logging.warning(f"Incorrect full name from {user_name}{user_id}")#, filename="log_bot.log")
        await message.answer(text="Напишите свое ФИО корректно")
        return
    else:
        for char in text_for_transp.lower():
            if char in letters:
                result.append(letters[char])
            else:
                result.append(char)
    logging.info(f"Success translitration from {text_for_transp} to {"".join(result).title()}")#, filename="log_bot.log")
    return message.answer(text="".join(result).title())


if __name__ == "__main__":
    dp.run_polling(bot)