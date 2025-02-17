from config import BOT_TOKEN, WEBHOOK_URL
from BotLogic.bot import  YannaBot
import config
import logging


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == "__main__":
 yanna = YannaBot(BOT_TOKEN)
 if config.BOT_TOKEN == 'YOUR_BOT_TOKEN':
     print("please modify config.py to include your bot token")
 else:
    yanna.Start()