import random

from telebot import TeleBot, custom_filters, StateMemoryStorage
from telebot.types import Message

import messages
from configs import BOT_TOKEN, MATH_QUESTIONS, PROGRAMMING_QUESTIONS

state_storage = StateMemoryStorage()

bot = TeleBot(BOT_TOKEN, state_storage=state_storage)

@bot.message_handler(commands=['start'])
def start(message: Message) -> None:
    bot.send_message(message.chat.id, messages.START_MESSAGE)


@bot.message_handler(commands=['math'])
def math(message: Message) -> None:
    question_id = random.choice(list(MATH_QUESTIONS.keys()))
    question = MATH_QUESTIONS[question_id]

    bot.set_state(message.from_user.id, {'question_id': question_id, 'category': 'math'})
    bot.send_message(message.from_user.id, question['prompt'])

@bot.message_handler(commands=['prog'])
def prog(message: Message) -> None:
    question_id = random.choice(list(PROGRAMMING_QUESTIONS.keys()))
    question = PROGRAMMING_QUESTIONS[question_id]

    bot.set_state(message.from_user.id, {'question_id': question_id, 'category': 'prog'})
    bot.send_message(message.from_user.id, question['prompt'])

@bot.message_handler(state='*')
def answer(message: Message) -> None:
    user_state = bot.get_state(message.from_user.id)
    if user_state is None:
        return

    question_id = user_state['question_id']
    category = user_state['category']

    if category == "math":
        question = MATH_QUESTIONS[question_id]
        if message.text.strip() == question['answer']:
            bot.send_message(message.from_user.id, messages.CORRECT_MATH_ANSWER)
            return

        bot.send_message(message.from_user.id, messages.INCORRECT_ANSWER)
    elif category == "prog":
        question = PROGRAMMING_QUESTIONS[question_id]
        if message.text.strip() == question['answer']:
            bot.send_message(message.from_user.id, messages.CORRECT_PROG_ANSWER)
            return

        bot.send_message(message.from_user.id, messages.INCORRECT_ANSWER)


def main():
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.infinity_polling()


if __name__ == '__main__':
    main()
