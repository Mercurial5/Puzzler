from os import environ

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = environ['BOT_TOKEN']

MATH_QUESTIONS = {
    1: {
        'prompt': 'x = 5 - 3. What is x?',
        'answer': '2'
    }
}
