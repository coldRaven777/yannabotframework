import logging
from telegram import Update, Chat, ChatMember, ForceReply
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

from .brain import Brain

'''logging stuff'''


'''The Class per se'''

class YannaBot:
    def __init__(self, token):
        self.token = token
        self.application = ApplicationBuilder().token(self.token).build()
        self.application.add_handler(MessageHandler(filters.TEXT, callback=self.ChatRepeater))
        self.logger = logging.basicConfig(
                                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                        level=logging.INFO)


    async def ChatRepeater(self,update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_name = update.effective_user.username
        chat = update.effective_chat
      
        if chat.type != Chat.PRIVATE or chat.id in context.bot_data.get("user_ids", set()):
            return
        await update.message.reply_html(
            f"Hello, {user_name}! I'm Yanna, your personal assistant. How can I help you today?",
            reply_markup=ForceReply(selective=True)
        )


    def Start(self):
        self.application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.ChatRepeater))
        self.application.run_polling()
        





