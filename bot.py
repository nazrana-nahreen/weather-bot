"""
bot.py — The main bot file.
This is where Telegram talks to your Python code.

How it works:
  User sends a message → Telegram sends it to this script → 
  we fetch weather → we send a reply back to the user.
"""
import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from weather import get_weather
from dotenv import load_dotenv

# Load your secret keys from the .env file
load_dotenv()

# This sets up logging so you can see what's happening when the bot runs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ─────────────────────────────────────────
# COMMAND: /start
# Runs when a user first opens the bot
# ─────────────────────────────────────────
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name  # Get the user's first name
    await update.message.reply_text(
        f"👋 Hi {name}! I'm your Weather Bot.\n\n"
        "Just send me any city name and I'll tell you the current weather!\n\n"
        "Example: London\n"
        "Example: Dhaka\n"
        "Example: New York\n\n"
        "Try it now! 🌤"
    )


# ─────────────────────────────────────────
# COMMAND: /help
# Runs when a user sends /help
# ─────────────────────────────────────────
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🆘 How to use this bot:\n\n"
        "1. Simply type any city name\n"
        "2. I'll reply with the current weather\n\n"
        "Commands:\n"
        "/start — Welcome message\n"
        "/help  — Show this help\n"
        "/about — About this bot"
    )


# ─────────────────────────────────────────
# COMMAND: /about
# ─────────────────────────────────────────
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Weather Bot\n\n"
        "Built with Python by a developer learning AI engineering.\n"
        "Powered by OpenWeatherMap API.\n\n"
        "Tech stack: Python · python-telegram-bot · REST API · Render"
    )


# ─────────────────────────────────────────
# MESSAGE HANDLER
# Runs when a user sends any regular text (not a command)
# This is the main feature — city name → weather reply
# ─────────────────────────────────────────
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = update.message.text.strip()  # Get what the user typed

    # Tell the user we're working on it (shows "typing..." in Telegram)
    await update.message.chat.send_action("typing")

    # Fetch the weather for this city
    result = get_weather(city)

    # Send the result back to the user
    await update.message.reply_text(result)


# ─────────────────────────────────────────
# MAIN — Start the bot
# ─────────────────────────────────────────
def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        print("❌ ERROR: TELEGRAM_BOT_TOKEN not found in .env file!")
        print("   Please add it. See README.md for instructions.")
        return

    print("✅ Bot is starting...")
    print("   Open Telegram and message your bot to test it!")
    print("   Press Ctrl+C to stop.\n")

    # Build the bot application
    app = ApplicationBuilder().token(token).build()

    # Register all the command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))

    # Register the message handler (for city names)
    # filters.TEXT means: any text message that is NOT a command
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start polling — this keeps the bot running and checking for messages
    app.run_polling()


# This means: only run main() if we run this file directly
if __name__ == "__main__":
    main()
