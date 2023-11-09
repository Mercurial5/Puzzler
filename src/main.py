import random

from telebot import TeleBot, custom_filters, StateMemoryStorage
from telebot.types import Message

import messages
from configs import BOT_TOKEN, MATH_QUESTIONS

state_storage = StateMemoryStorage()

bot = TeleBot(BOT_TOKEN, state_storage=state_storage)


@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    bot.send_message(message.chat.id, messages.START_MESSAGE)


@bot.message_handler(commands=['math'])
def math(message: Message) -> None:
    question_id = random.choice(list(MATH_QUESTIONS.keys()))
    question = MATH_QUESTIONS[question_id]

    bot.set_state(message.from_user.id, question_id)
    bot.send_message(message.from_user.id, question['prompt'])


@bot.message_handler(state='*')
def answer(message: Message) -> None:
    user_state = bot.get_state(message.from_user.id)
    if user_state is None:
        return

    question = MATH_QUESTIONS[user_state]
    if message.text.strip() == question['answer']:
        bot.send_message(message.from_user.id, messages.CORRECT_MATH_ANSWER)
        return

    bot.send_message(message.from_user.id, messages.INCORRECT_ANSWER)


def main():
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()


if __name__ == '__main__':
    main()
