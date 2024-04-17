from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from xlsx import reading_xlsx
from settings import BOT_KEY

def start(update, context):
    update.message.reply_text('Прикрепите Excel файл!')


def help(update, context):
    update.message.reply_text("Вам нужно прикрепить файл формата 'xlsx'.")


def echo(update, context):
    update.message.reply_text("Напишите /help, если не знаете что делать.")

def download(update,context):
    downloader = context.bot.getFile(update.message.document.file_id)
    if downloader["file_path"].lower().endswith(".xlsx"):
        filename = downloader.download()
        update.message.reply_text("Отправка файлов началась!\n")
        emails_count = reading_xlsx(filename)
        update.message.reply_text(f'Количество отправленных писем = {emails_count}')
    else:
        update.message.reply_text("Неверный формат файла. Попробуйте ещё раз.")


def main():
    """Start the bot."""
    updater = Updater(BOT_KEY, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(MessageHandler(Filters.document, download))

    dp.add_handler(MessageHandler(Filters.text, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
