from cgitb import text
import logging
from typing import Any
from aiogram import Bot, Dispatcher, executor, types
import os


BOT_TOKEN = os.environ.get('BOT_TOKEN')
# 


# Объект бота
bot = Bot(token=BOT_TOKEN)
# Диспетчер для бота

dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(filename="bot.log", 
                    level=logging.INFO,
                    format='%(asctime)s %(message)s'
                    )

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.answer('Привет!\nЭтот бот написал @vadych.\nЕдинственное, что я умею - повторять за тобой')
    
    
# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    logging.info('Комманда \\test1 от %s(%s)', message.from_user.full_name, message.from_user.mention)
    print(message.text)
    await message.reply("Test 1")


@dp.message_handler(content_types=[types.ContentType.ANY])
async def cmd_all(message: types.Message):
    answer = message.text or message.caption
    logging.info('%s %s от %s(%s)',
                 message.content_type,
                 answer,
                 message.from_user.full_name, 
                 message.from_user.mention)
    await message.answer(answer)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
bot.send_message()