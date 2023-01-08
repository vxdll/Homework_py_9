# Функции калькулятора для бота

from logger import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def ration_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split()
    x = float(item[1])
    oprd = str(item[2])
    y = float(item[3])
    if oprd == "+":
        res = x + y
        z = output(res)
        await update.message.reply_text(f'{x} + {y} = {z}')
    elif oprd == "-":
        res = x - y
        z = output(res)
        await update.message.reply_text(f'{x} - {y} = {z}')
    elif oprd == "*":
        res = x * y
        z = output(res)
        await update.message.reply_text(f'{x} * {y} = {z}')
    elif oprd == "/":
        if y == 0:
            await update.message.reply_text("Ошибка!!! На ноль делить запрещено!")
        else:
            res = x / y
            z = output(res)
            await update.message.reply_text(f'{x} / {y} = {z}')
    else:
        await update.message.reply_text("Ошибка")

async def complex_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    item = msg.split()
    x = complex(item[1])
    oprd = str(item[2])
    y = complex(item[3])
    if oprd == "+":
        await update.message.reply_text(f'{x} + {y} = {x + y}')
    elif oprd == "-":
        await update.message.reply_text(f'{x} - {y} = {x - y}')
    elif oprd == "*":
        await update.message.reply_text(f'{x} * {y} = {x * y}')
    elif oprd == "/":
        await update.message.reply_text(f'{x} / {y} = {x / y}')

def output(result):
    try:
        if result.is_integer():
            x = int(result)
        elif isinstance(result, float):
            x = float(result)
        else:
            x = result
    except:
        x = result
    return x

