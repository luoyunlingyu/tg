from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# 你的Bot的Token
TOKEN = '6877106792:AAFFEd4G9Shu33m0WBhWjEcL1iTE6l8lrRs'

def start(update, context):
    """发送一条欢迎消息当命令/start被 issued."""
    update.message.reply_text('Hi! I am a simple Telegram Bot. Send me a message and I will reply the same to you.')

def echo(update, context):
    """回复用户发送的消息."""
    update.message.reply_text(update.message.text)

def main():
    """启动机器人."""
    updater = Updater(TOKEN, use_context=True)

    # 获取dispatcher以注册处理器
    dp = updater.dispatcher

    # 注册处理器
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # 开始轮询
    updater.start_polling()

    # 运行直到按下Ctrl-C或程序被进程杀死
    updater.idle()

if __name__ == '__main__':
    main()
