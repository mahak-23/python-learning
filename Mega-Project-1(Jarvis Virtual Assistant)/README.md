# 🤖 JARVIS - AI-Powered Virtual Assistant

A sophisticated voice-activated AI assistant. This project demonstrates advanced Python concepts including OpenAI integration, speech processing, and automation.

## ✨ Advanced Features

- **🧠 OpenAI GPT Integration**: Intelligent responses using GPT-3.5-turbo
- **🎤 Wake Word Detection**: Responds to "Jarvis" wake word
- **🔊 Dual TTS Systems**: Both pyttsx3 and Google TTS with pygame
- **🌐 Smart Web Browsing**: Voice-controlled website opening
- **🎵 Music Library**: YouTube music integration with voice commands
- **📰 News Integration**: Real-time news headlines via News API
- **🎯 Voice Command Processing**: Natural language understanding

## 📋 Prerequisites & Setup

### **1. Install Required Packages**
```bash
pip install -r requirements.txt
```

### **2. API Keys Setup**
You'll need API keys for full functionality:

**🔑 OpenAI API Key** (Required for AI responses)
1. Sign up at [OpenAI](https://platform.openai.com)
2. Create API key
3. Replace `<Your OpenAI Key Here>` in `main.py`

**📰 News API Key** (Optional for news features)
1. Sign up at [NewsAPI](https://newsapi.org)
2. Get free API key
3. Replace `<Your News API Key Here>` in `main.py`

### **3. Special Installation Notes**
**Windows users**: For PyAudio issues:
```bash
pip install pipwin
pipwin install pyaudio
```

**Linux users**: Install system dependencies:
```bash
sudo apt-get install espeak espeak-data libespeak1 libespeak-dev
sudo apt-get install ffmpeg
```

## 🚀 Usage

1. **Run the assistant:**
   ```bash
   python main.py
   ```

2. **Voice Commands:**
   - "Hello Jarvis" - Wake up the assistant
   - "What time is it?" - Get current time
   - "What's the date?" - Get current date
   - "Search Python programming" - Web search
   - "Play music" - Open music application
   - "Open calculator" - Launch calculator
   - "Goodbye" - Exit the assistant

## 🛠️ Customization

- **Voice Speed**: Modify `rate` property in `__init__` method
- **Add Commands**: Extend `process_command` method
- **Response Phrases**: Update speaking responses
- **Applications**: Add more apps in `open_application` method

## 🔧 Troubleshooting

- **Microphone Issues**: Check microphone permissions
- **Speech Recognition Errors**: Ensure internet connection
- **Missing Dependencies**: Install all required packages

## 📚 Learning Concepts

This project demonstrates:
- **Speech Recognition**: Converting speech to text
- **Text-to-Speech**: Converting text to speech
- **API Integration**: Web requests and responses
- **File Operations**: System file handling
- **Error Handling**: Managing exceptions gracefully
- **Class-based Programming**: Object-oriented design

## 🎓 Educational Value

this project showcases:
- Advanced Python concepts
- Real-world application development
- Integration of multiple libraries
- Voice interface programming
