from config import LOG_GROUP_ID
from PandapiesUserBot import bot, Pandapies

if __name__ == "__main__":
    Pandapies.start()
    bot.run()
    with bot:
        bot.send_message(f"{LOG_GROUP_ID}", "Grrrr Panda Ready Boi!")
