#              Задача
#  Прикрутить бота к задачам с предыдущего семинара:
#  Создать калькулятор для работы с рациональными и 
#  комплексными числами, организовать меню, добавив в неё систему логирования
#
#         Программа:





from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *


app = ApplicationBuilder().token("введите сдесь свой токкен").build()          #  введите сдесь свой токкен

app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("formula", formula_command))

print('сервер запущен')
app.run_polling()