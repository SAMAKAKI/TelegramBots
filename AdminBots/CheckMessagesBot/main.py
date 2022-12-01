# import libraries
from telebot import *
from TOKEN import TOKEN

# main function
def telegram_bot(_TOKEN):
    # create variable bot
    bot = TeleBot(_TOKEN, parse_mode='html')

    # decorate function / this function will work if you write text
    @bot.message_handler(content_types=['text'])
    # function which check text in message if in message is word from list "curse_words" delete this message
    def check_messages(message):
        curse_words = ["сука", "блять", "блядь", "хуй", "пизда"]
        for word in curse_words:
            if word in message.text.lower():
                bot.delete_message(message.chat.id, message.id)
                # bot.send_message()

    # decorate function / this function will work if you add or delete user in your group or you changed title group or you changed photo
    @bot.message_handler(content_types=['new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo'])
    def delete_join_message(message):
        bot.delete_message(message.chat.id, message.id)


    # function which enables work none stop
    bot.polling(none_stop=True)

# running the program
if __name__ == '__main__':
    telegram_bot(TOKEN)
