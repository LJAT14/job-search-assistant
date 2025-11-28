@echo off
echo 🤖 Setting up Job Bot Pro...

REM Create directories
echo 📁 Creating directories...
if not exist logs mkdir logs
if not exist data mkdir data
if not exist config mkdir config

REM Create .env from template
if not exist .env (
    echo 📝 Creating .env file...
    copy .env.template .env
    echo ✅ .env created! Please edit it with your API keys.
) else (
    echo ⚠️  .env already exists, skipping...
)

REM Install Python packages
echo 📦 Installing dependencies...
pip install -r requirements.txt

echo.
echo ✅ Setup complete!
echo.
echo 📋 Next steps:
echo 1. Get Groq API key: https://console.groq.com
echo 2. Get CallMeBot API key: Send 'I allow callmebot to send me messages' to +34 644 59 71 47
echo 3. Edit .env file with your API keys
echo 4. Run: streamlit run app.py
echo.
echo 🚀 Happy job hunting!
pause