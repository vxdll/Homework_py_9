from bot_calculator_commands import *
from another_bot_commands import *
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("YOUR TOKEN").build()

print("start server") # Вывод в консоль для проверки работы бота

app.add_handler(CommandHandler("hi", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("manual", manual))
app.add_handler(CommandHandler("complex", complex_calc))
app.add_handler(CommandHandler("rational", ration_calc))
app.run_polling()




