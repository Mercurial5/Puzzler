from os import environ

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = environ['BOT_TOKEN']

PROGRAMMING_QUESTIONS = {
    1: {
        'prompt': 'where is correct if?\n'
                  '\n'
                  '1. <if></if>\n'
                  '2. <if><if>\n'
                  '3. if ()\n'
                  '4. if ( ) { }',
        'answer': '4',
    },
    2: {
        'prompt': 'where is correct div?\n'
                  '\n'
                  '1. <div></div>\n'
                  '2. <div><div>\n'
                  '3. div/div\n'
                  '4. div{}\n',
        'answer': '1',
    }
}
MATH_QUESTIONS = {
    1: {
        'prompt': 'x = 5 - 3. What is x?',
        'answer': '2'
    },
    2: {
        'prompt': 'x = 2y/2. What is x?',
        'answer': 'y'
    },
    3: {
        'prompt': 'x = 6 - 2. What is x?',
        'answer': '4'
    }
}
