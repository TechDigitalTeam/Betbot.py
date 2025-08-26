from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random

# Your bot token from BotFather
TOKEN = "8403760567:AAGiKlsT2HDtKLnC2fgMwCx0jqNyAg2TkiU"

# Command: /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to BetBot! Use /bet <amount> <number> to place a bet. Pick a number between 1-10. Win 2x your bet if you guess right!"
    )

# Command: /bet <amount> <number>
async def bet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Extract amount and number from command
        args = context.args
        if len(args) != 2:
            await update.message.reply_text("Usage: /bet <amount> <number>")
            return

        amount = float(args[0])
        number = int(args[1])

        # Validate inputs
        if number < 1 or number > 10:
            await update.message.reply_text("Pick a number between 1 and 10!")
            return
        if amount <= 0:
            await update.message.reply_text("Bet amount must be positive!")
            return

        # Simulate a random result
        result = random.randint(1, 10)
        if number == result:
            winnings = amount * 2
            await update.message.reply_text(
                f"🎉 Congrats! The number was {result}. You won {winnings}!"
            )
        else:
            await update.message.reply_text(
                f"😞 Sorry! The number was {result}. You lost {amount}."
            )

    except ValueError:
        await update.message.reply_text("Invalid input! Use /bet <amount> <number>")

# Main function to run the bot
def main():
    app = Application.builder().token(TOKEN).build()

    # Add handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("bet", bet))

    # Start the bot
    app.run_polling()

if name == "main":
    main()
