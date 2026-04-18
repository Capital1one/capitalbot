from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os
import random

# ---------- START ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hey 👋 Welcome!\n\n"
        "I’m your Tesla & market info bot 📊\n"
        "I help explain TSLA and general market updates.\n\n"
        "Commands you can use:\n"
        "/tesla - Tesla overview\n"
        "/group - join learning community info"
    )

# ---------- TESLA INFO (natural responses) ----------
async def tesla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    responses = [
        "📊 Tesla (TSLA) moves a lot based on news, earnings, and EV demand.\nWant a simple or detailed breakdown?",
        "⚡ TSLA is heavily influenced by Elon Musk updates and market sentiment.\nAre you tracking short-term or long-term?",
        "📈 Tesla is a high-volatility stock in the EV/tech sector.\nWant today’s quick market summary?",
        "👀 I can break Tesla down simply or explain deeper trends—what do you prefer?"
    ]
    await update.message.reply_text(random.choice(responses))

# ---------- GROUP INFO ----------
async def group(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📚 Tesla & Market Learning Community\n\n"
        "This is a space for:\n"
        "• Long-term investing discussions\n"
        "• Short-term market updates\n"
        "• Beginner-friendly stock learning\n"
        "• Tesla & tech market analysis\n\n"
        "⚠️ Educational content only — no guaranteed results.\n\n"
        "If you want to join, ask the admin or check the pinned link in our group."
    )

# ---------- BOT SETUP ----------
app = Application.builder().token(os.getenv("BOT_TOKEN")).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("tesla", tesla))
app.add_handler(CommandHandler("group", group))

app.run_polling()
if __name__ == "__main__":
    app.run_polling()
