# Различные функции для бота

from logger import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Привет {update.effective_user.first_name}, это первый бот который написал '
                                    f'Григорий Васякин, для ознакомления с его возможностями нажми /help или напиши '
                                    f'эту команду в чате!!! ')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/manual\n/complex\n/rational\n/help')

async def manual(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'КАК РАБОТАТЬ С БОТОМ\nДанный бот представляет из себя калькулятор с 2мя '
                                    f'функциями\n'
                                    f'1) Калькулятор комплексных чисел /complex\n'
                                    f'2) Калькулятор рациональных чисел /rational\n'
                                    f'Все числа нужно указывать без пробелов, пробелом с двух сторон отделяется '
                                    f'оператор арифметического действия над числами\n'
                                    f'Пример:\n'
                                    f'/complex 33+8j * 2+3j\n'
                                    f'/rational 1640 / 2 \n'
                                    f'и.т.д.')

