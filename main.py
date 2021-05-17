import requests
from datetime import datetime
import telebot
from auth_data import token


def get_data():
    req = requests.get(" https://yobit.net/api/3/ticker/btc_usd")
    response = req.json()
    sell_price = response["btc_usd"]["sell"]
    print(f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell BTC price: "
          f"{sell_price}")


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_massage(message.chat.id, "Hello friend! Write the 'price' "
                                          "to find out cost of BTC ")

    @bot.message_handler(content_type=['text'])
    def send_text(message):
        if message.text.lower() == "price":
            try:
                req = requests.get(" https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price = response["btc_usd"]["sell"]
                bot.send_message(
                    message.chat.id,
                    f"{datetime.now().strftime('%d-%m-%Y %H:%M')}\nSell BTC price: "
                    f"{sell_price}"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Damn...Something was wrong..."
                )
        else:
            bot.send_message(message.chat.id, "Whaat? Check the command!")

    bot.polling()


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)
