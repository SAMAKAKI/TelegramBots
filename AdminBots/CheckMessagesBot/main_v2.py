import time
import TOKEN
import logging
from aiogram import Bot, Dispatcher, executor, types
from filtres import IsAdminFilter

#log level
logging.basicConfig(level=logging.INFO)

#bot init
bot = Bot(token=TOKEN.TOKEN)
dp = Dispatcher(bot)
dp.filters_factory.bind(IsAdminFilter)

def telegram_bot():
    @dp.message_handler(commands=['spam'], commands_prefix="!/")
    async def spam_message(message: types.Message):
        for i in range(1, 3):
            await message.answer(message.text.strip('/spam'))
            time.sleep(0.3)

    # @dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
    # async def cmd_ban(message: types.Message):
    #     if not message.reply_to_message:
    #         await message.reply("This commands must be answer to message")
    #         return
    #     await message.bot.delete_message(TOKEN.GROUP_ID, message.message_id)
    #     await message.bot.kick_chat_member(chat_id=TOKEN.GROUP_ID, user_id=message.reply_to_message.from_user.id)
    #     await message.reply_to_message.reply("User has banned")

    @dp.message_handler(content_types=['text'])
    async def check_messages(message: types.Message):
        curse_words = ["сука", "блять", "блядь", "хуй", "пизда", "гандон", "еблан", "пидорас"]
        for word in curse_words:
            if word in message.text.lower():
                await message.delete()

    @dp.message_handler(content_types=['new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo'])
    async def delete_join_message(message):
        await message.delete()

    executor.start_polling(dp, skip_updates=True)

if __name__ == '__main__':
    telegram_bot()
