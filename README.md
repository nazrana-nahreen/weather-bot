# Weather Bot 🌤

A Telegram bot that tells you the current weather for any city in the world.
Built with Python. Deployed free on Render. 100% free to run.

---

## How it looks when running

```
You:  London
Bot:  ☁️ Weather in London, GB
      ──────────────────────────────
      🌡  Temperature:  14°C (feels like 11°C)
      🌤  Condition:    Overcast clouds
      💧  Humidity:     78%
      💨  Wind:         19 km/h
      ──────────────────────────────
      💡 Have a great day! 😊
```

---

## Files explained (read this first!)

```
weather_bot/
├── bot.py           ← The main file. Handles Telegram messages.
├── weather.py       ← Fetches weather from OpenWeatherMap API.
├── requirements.txt ← List of Python packages to install.
├── .env.example     ← Template for your secret keys.
├── render.yaml      ← Tells Render.com how to run your bot.
└── README.md        ← This file!
```

---

## Step 1 — Create your Telegram Bot (5 minutes)

1. Open Telegram on your phone or computer
2. Search for `@BotFather` (it has a blue checkmark ✓)
3. Send it the message: `/newbot`
4. It will ask for a name → type something like: `My Weather Bot`
5. It will ask for a username → type something like: `myweather_bot`
   (must end in "bot", must be unique)
6. BotFather will give you a token that looks like:
   `7123456789:AAHdq_example_token_here`
7. **Copy and save this token** — you'll need it in Step 4

---

## Step 2 — Get a free OpenWeatherMap API key (5 minutes)

1. Go to https://openweathermap.org
2. Click **Sign Up** (top right) — it's free
3. Fill in your name, email, password → click **Create Account**
4. Check your email and verify your account
5. Log in → click your username (top right) → click **My API Keys**
6. You'll see a key already created — copy it
   It looks like: `a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4`
7. **Important:** Wait 10 minutes before using it (new keys take time to activate)

---

## Step 3 — Install Python and packages

First, make sure you have Python installed:
```bash
python --version
```
If you see `Python 3.10` or higher, you're good. If not, download it from https://python.org

Install the required packages:
```bash
pip install -r requirements.txt
```

---

## Step 4 — Set up your secret keys

1. In your project folder, copy the example file:

**On Windows:**
```bash
copy .env.example .env
```

**On Mac/Linux:**
```bash
cp .env.example .env
```

2. Open the `.env` file with any text editor (Notepad, VS Code, etc.)

3. Replace the placeholder values with your real keys:

```
TELEGRAM_BOT_TOKEN=7123456789:AAHdq_your_real_token_here
OPENWEATHER_API_KEY=a1b2c3d4e5f6your_real_key_here
```

4. Save the file.

---

## Step 5 — Run the bot locally (test it!)

```bash
python bot.py
```

You should see:
```
✅ Bot is starting...
   Open Telegram and message your bot to test it!
   Press Ctrl+C to stop.
```

Now open Telegram, find your bot by its username, and send it `/start`.
Then try typing a city like `Dhaka` or `London`.

If it replies with weather — everything is working! 🎉

Press `Ctrl+C` to stop the bot.

---

## Step 6 — Deploy to Render (make it live 24/7 for free!)

This puts your bot on the internet so it runs forever, even when your PC is off.

### 6a. Put your code on GitHub

1. Go to https://github.com and create a free account
2. Click the **+** button → **New repository**
3. Name it `weather-bot` → click **Create repository**
4. Follow GitHub's instructions to upload your files

   **Important:** Add a `.gitignore` file to protect your secrets:
   Create a file called `.gitignore` and add this line:
   ```
   .env
   ```
   This stops your secret `.env` file from being uploaded!

### 6b. Deploy on Render

1. Go to https://render.com and create a free account
2. Click **New +** → **Web Service** (or **Background Worker**)
3. Connect your GitHub account when asked
4. Select your `weather-bot` repository
5. Render will detect `render.yaml` automatically — click **Create Service**
6. Now add your secret keys:
   - Click **Environment** in the left menu
   - Add `TELEGRAM_BOT_TOKEN` → paste your token
   - Add `OPENWEATHER_API_KEY` → paste your key
7. Click **Save Changes** → Render will restart your bot
8. Your bot is now live 24/7! 🎉

---

## Troubleshooting

**"No module named telegram"**
→ Run: `pip install -r requirements.txt`

**"TELEGRAM_BOT_TOKEN not found"**
→ Make sure your `.env` file exists and has the token filled in (not the example text)

**Bot doesn't reply to city names**
→ Your OpenWeatherMap key might need more time to activate. Wait 10 minutes and try again.

**"City not found"**
→ Check spelling. Try the English name of the city (e.g. "Munich" not "München")

---

## What to write on your CV

> **Telegram Weather Bot** | Python, REST APIs, Cloud Deployment
> Built and deployed a live Telegram bot that fetches real-time weather data 
> for any city using the OpenWeatherMap REST API. Deployed 24/7 on Render cloud 
> hosting. Available at t.me/yourbotusername

Skills to list:
- Python (async programming, modules, API integration)
- REST API consumption (HTTP requests, JSON parsing)
- Bot development (python-telegram-bot)
- Cloud deployment (Render)
- Environment variable management & secret handling
- Git & GitHub

---

## Ideas to make it even better (for a stronger CV)

Once this is working, try adding:

1. `/forecast` command — show 5-day forecast
2. `/setcity London` — let users save a default city
3. Scheduled alerts — send weather every morning automatically
4. Add AI summaries using Gemini free API

Each addition = a new bullet point on your CV! 💪

---

*Built as a learning project. Total cost: $0.*
