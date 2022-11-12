from telegram.ext import Updater, CallbackContext, CommandHandler, Filters, MessageHandler
import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup

TOKEN = '5794354224:AAHGxeZdBWvP6Tpp6i6X-UTl3DlDmPKfl7s'
updater = Updater(token = TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format ="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO )

#------------блок функций-----------------------------------

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id = update.effective_chat.id, text = 'Для появления всплывающего меню наберите /menu')

def complex_nums(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id = update.effective_chat.id, text = 'Выберите нужну. операцию из выпадающего меню')

def text(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text='чтобы увидеть мои возможности наберите /menu')


#--------------блок создания кнопок--------------------------
def complex_multy(update: Update, context: CallbackContext):
    ls = context.args
    print(ls)
    context.bot.send_message(chat_id=update.effective_chat.id, text='введите /multy и через пробел два числа')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'произведение чисел равно {int(ls[0]) * int(ls[1])}')



def reply_button(update: Update, context: CallbackContext):

    custom_keyboards = [['/complex', '/вещественные']]
    reply_keyboard = ReplyKeyboardMarkup(custom_keyboards)
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'операции над какими числами будете проводить?', reply_markup = reply_keyboard)

def reply_complex_button(update: Update, context: CallbackContext):

    custom_keyboards = [['/summa', '/dif'], ['/multy', '/division']]
    reply_keyboard = ReplyKeyboardMarkup(custom_keyboards)
    context.bot.send_message(chat_id=update.effective_chat.id, text = 'выберите действие над вумя числами', reply_markup = reply_keyboard)

def complex_summa(update: Update, context: CallbackContext):
    ls = context.args
    print(ls)
    context.bot.send_message(chat_id=update.effective_chat.id, text='введите /summa и через пробел два числа')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'сумма чисел равна {int(ls[0]) + int(ls[1])}')


def complex_difference(update: Update, context: CallbackContext):
    ls = context.args
    print(ls)
    context.bot.send_message(chat_id=update.effective_chat.id, text='введите /dif и через пробел два числа')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'разность чисел равна {int(ls[0]) - int(ls[1])}')

def complex_division(update: Update, context: CallbackContext):
    ls = context.args
    print(ls)
    context.bot.send_message(chat_id=update.effective_chat.id, text='введите /division и через пробел два числа')
    context.bot.send_message(chat_id=update.effective_chat.id, text=f'частное двух чисел равно {int(ls[0])/int(ls[1])}')

#------------блок переменных класса CommandHandler-----------------
complex_division_handler = CommandHandler('division', complex_division)
complex_multy_handler = CommandHandler('multy', complex_multy)   # /multy
complex_difference_handler = CommandHandler('dif', complex_difference)   # /dif
complex_summa_handler = CommandHandler('summa', complex_summa)   # /summa
reply_complex_button_handler = CommandHandler('complex', reply_complex_button)  # /complex
reply_button_handler = CommandHandler('menu', reply_button)  # /menu
start_handler = CommandHandler('start', start)   # /start
text_handler = MessageHandler(Filters.text, text)     #  /любой текст



#-------------блок выполнения команд диспетчером-------------------
dispatcher.add_handler(complex_division_handler)
dispatcher.add_handler(complex_difference_handler)
dispatcher.add_handler(complex_summa_handler)
dispatcher.add_handler(reply_complex_button_handler)
dispatcher.add_handler(reply_button_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

updater.start_polling()