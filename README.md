[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/a2pucUEo)

# 📚 Study Buddy AI Assistant

An intelligent AI-powered study companion built with Streamlit and Groq API, featuring multiple personality modes to match your learning style.

## ✨ Features

- 🤖 **3 AI Personalities**: Choose between Friendly, Professional, or Humorous modes
- 💬 **Real-time Chat**: Streaming responses for natural conversations
- 📖 **Study-Focused**: Designed specifically for learning and academic support
- 🎨 **Clean Interface**: Beautiful, emoji-rich UI with Streamlit
- ⚡ **Fast Responses**: Powered by Groq's llama-3.3-70b-versatile model

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Groq API key (get one free at [console.groq.com](https://console.groq.com/keys))

### Local Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/CodeCubCA/ai-chatbox-Alex-CodeCub.git
   cd ai-chatbox-Alex-CodeCub
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env

   # Edit .env and add your Groq API key
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

## ☁️ Deploying to Streamlit Cloud

### Step 1: Fork or Push to GitHub
Ensure your code is pushed to a GitHub repository.

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io/)
2. Click "New app"
3. Select your repository and branch
4. Set main file path: `app.py`
5. Click "Deploy"

### Step 3: **IMPORTANT - Add Secrets**

Your app **will not work** without adding the Groq API key:

1. Click on your deployed app
2. Go to **Settings** → **Secrets**
3. Add the following:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   ```
4. Click **Save**
5. The app will automatically reboot

## 🎭 AI Personalities

### 😊 Friendly
- Warm and encouraging tone
- Like chatting with a supportive friend
- Uses positive language and emojis
- Great for motivation and gentle guidance

### 🎓 Professional
- Rigorous and accurate
- Structured, well-organized answers
- Academic and professional tone
- Best for serious study and research

### 😄 Humorous
- Light and entertaining
- Makes learning fun with humor
- Uses analogies and witty remarks
- Perfect for keeping study sessions engaging

## 📖 What Can Study Buddy Help With?

- 📖 Answering study questions
- 💡 Explaining complex concepts
- ✍️ Tutoring homework and essays
- 🎯 Creating study plans
- 📝 Summarizing and reviewing topics
- 🧠 Providing learning method suggestions

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Groq API (llama-3.3-70b-versatile)
- **Language**: Python 3.13+
- **Dependencies**: See [requirements.txt](requirements.txt)

## 📁 Project Structure

```
ai-chatbox/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example       # Environment variables template
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

## 🔑 Getting a Groq API Key

1. Visit [console.groq.com](https://console.groq.com/)
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. Copy and save it securely

## 🐛 Troubleshooting

### App stuck on "Creating" in Streamlit Cloud
- **Solution**: Make sure you've added `GROQ_API_KEY` in the app's Secrets settings

### "GROQ_API_KEY is missing" error
- **Local**: Check your `.env` file exists and contains the key
- **Cloud**: Add the key in Settings → Secrets

### Dependencies installation fails
- Try upgrading pip: `python -m pip install --upgrade pip`
- Use: `python -m pip install -r requirements.txt`

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👤 Author

**Alex-CodeCub**
- GitHub: [@alex-codecub](https://github.com/alex-codecub)
- Email: alex@codecub.org

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Groq](https://groq.com/)
- AI assistance from [Claude Code](https://claude.com/claude-code)

---

**Happy Learning! 📚✨**
