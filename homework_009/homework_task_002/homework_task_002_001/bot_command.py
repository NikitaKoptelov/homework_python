from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sympy


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'привет. это список команд:\n'+
                                    '/hello - приветствие\n'+
                                    '/help - список команд\n'+
                                    '/formula - арифметическое вычисление выражений')

async def formula_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log_zapis = ''
    x = sympy.Symbol('x')
    y = sympy.Symbol('y')
    j = sympy.Symbol('j')
    msg = update.message.text
    log_zapis = f'введенные значения от пользователя - {msg}'
    wread_fail(log_zapis)
    items = msg.partition('/formula ')[2]
    rez = sympy.simplify(items)
    log_zapis = f'результат вычислений - {rez}'
    wread_fail(log_zapis)
    await update.message.reply_text(f'результат вычисления - {rez}')

def wread_fail(log_zapis):
    with open("D:/lesson_Python/homework_python/homework_009/homework_task_002/homework_task_002_001/log_vicheslen.txt", "a") as write_file:
        write_file.write(log_zapis + '\n')
