# Модуль логирования
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('bd.txt', 'a')
    file.write(f"{datetime.datetime.now().time()}, {update.effective_user.first_name}, {update.effective_user.id}, "
               f"{update.message.text}\n")
    file.close()