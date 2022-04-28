import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

link = "https://www.binance.com/en/markets/coinInfo"

reqs = requests.get(link)
soup = BeautifulSoup(reqs.content, "html.parser")
main = soup.find('div', class_='css-1vuj9rf')
list = main.find_all('div', class_='css-vlibs4')



def hi(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def web(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'https://codepn.uz')

def number(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'+998-93-179-71-79')


def coins(update: Update, context: CallbackContext) -> None:
    for i in range(0, 40):
        name = list[i].find('div', class_='css-1wp9rgv')
        stock = list[i].find('div', class_='css-ydcgk2')
        plus = list[i].find('div', class_='css-18yakpx')    
        update.message.reply_text(f'{name.text} {stock.text} {plus.text}')

def bit(update: Update, context: CallbackContext) -> None:
        name = list[0].find('div', class_='css-1wp9rgv')
        stock = list[0].find('div', class_='css-ydcgk2')
        plus = list[0].find('div', class_='css-18yakpx')    
        update.message.reply_text(f'{name.text} {stock.text} {plus.text}')

def eth(update: Update, context: CallbackContext) -> None:
        name = list[1].find('div', class_='css-1wp9rgv')
        stock = list[1].find('div', class_='css-ydcgk2')
        plus = list[1].find('div', class_='css-18yakpx')    
        update.message.reply_text(f'{name.text} {stock.text} {plus.text}')

updater = Updater('5306411965:AAEu6Dhgba_6fWtScjdqEqOETHvge0p_5bU')

updater.dispatcher.add_handler(CommandHandler('hello', hi))
updater.dispatcher.add_handler(CommandHandler('website', web))
updater.dispatcher.add_handler(CommandHandler('number', number))
updater.dispatcher.add_handler(CommandHandler('market', coins))
updater.dispatcher.add_handler(CommandHandler('BTC', bit))
updater.dispatcher.add_handler(CommandHandler('ETH', eth))



updater.start_polling()
updater.idle()
