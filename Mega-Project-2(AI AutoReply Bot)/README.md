# 💬 AI AutoReply Bot - Advanced Chat Automation

An advanced WhatsApp/chat automation system . This project demonstrates sophisticated screen automation, AI integration, and real-time chat processing.

## 🚀 Advanced Features

- **🤖 OpenAI GPT Integration**: Intelligent response generation using GPT-3.5-turbo
- **🖱️ Screen Automation**: Real-time chat monitoring using pyautogui
- **📱 WhatsApp Integration**: Automatic message detection and reply
- **🎯 Smart Message Detection**: Identifies when to respond
- **📋 Clipboard Operations**: Seamless text capture and sending
- **🧠 Context Understanding**: Analyzes full chat history for relevant responses
- **🎭 Personality Simulation**: Responds with configured personality traits

## 📋 Prerequisites & Setup

### **1. Install Required Packages**
```bash
pip install -r requirements.txt
```

### **2. OpenAI API Setup** 
**🔑 Required for AI responses:**
1. Sign up at [OpenAI Platform](https://platform.openai.com)
2. Create an API key
3. Replace `<Your Key Here>` in the Python files with your actual key

### **3. Screen Coordinate Setup**
**📐 Essential for automation:**
1. Run coordinate detector: `python 01_get_cursor.py`
2. Find coordinates for your screen resolution
3. Update coordinates in `main.py` if needed

## 🚀 Usage Options

### **Option 1: Full Auto-Bot**
```bash
python 03_bot.py
```
- Fully automated WhatsApp monitoring
- Real-time message detection and response
- Uses screen coordinates for automation

### **Option 2: Interactive Menu**
```bash
python main.py
```
Choose from:
1. Start Auto-Reply Bot
2. Setup Screen Coordinates  
3. Test OpenAI Integration
4. Get Current Mouse Coordinates

### **Option 3: Test Individual Components**
```bash
python 01_get_cursor.py    # Find screen coordinates
python 02_openai.py        # Test AI responses
```

## 💡 Supported Intents

| Intent | Example Messages | Response Type |
|--------|------------------|---------------|
| **Greeting** | "Hello", "Hi there", "Good morning" | Friendly welcomes |
| **Questions** | "What is...", "How do...", "Can you..." | Helpful information |
| **Thanks** | "Thank you", "Thanks a lot" | Gracious acknowledgments |
| **Compliments** | "Good job", "Amazing work" | Modest appreciation |
| **Help** | "I need help", "Can you assist" | Supportive guidance |
| **Goodbye** | "Bye", "See you later" | Warm farewells |

## 🎭 Sentiment Analysis

The bot recognizes three sentiment types:

- **😊 Positive**: Responds with enthusiasm
- **😔 Negative**: Shows empathy and understanding  
- **😐 Neutral**: Maintains friendly, helpful tone

## 📊 Features Showcase

### **Intent Detection Examples**
```python
"Hello there!" → Greeting Intent
"How does this work?" → Question Intent
"Thanks for your help!" → Thanks Intent
```

### **Sentiment Modification**
```python
"I'm really frustrated" → Negative → "I understand that might be frustrating..."
"This is amazing!" → Positive → "That's wonderful! ..."
```

### **Conversation Statistics**
- Total messages exchanged
- Most common intent patterns
- Overall conversation sentiment
- Learning insights

## 🛠️ Customization

### **Add New Response Categories**
```python
self.responses["custom_intent"] = [
    "Custom response 1",
    "Custom response 2"
]
```

### **Extend Intent Recognition**
```python
def detect_intent(self, message):
    # Add new pattern matching
    if re.search(r'\bnew_pattern\b', message_lower):
        return "new_intent"
```

### **Modify Sentiment Analysis**
```python
# Add more emotion keywords
positive_words = ["happy", "excited", "thrilled", ...]
negative_words = ["sad", "angry", "disappointed", ...]
```

## 📚 Learning Concepts

This project demonstrates:

- **Natural Language Processing**: Text analysis and understanding
- **Regular Expressions**: Pattern matching for intent detection
- **Sentiment Analysis**: Emotional tone detection
- **Data Structures**: Efficient response management
- **JSON Handling**: Conversation data storage
- **Object-Oriented Programming**: Clean, modular design

## 🎓 Educational Value

- **String Manipulation**: Advanced text processing
- **Conditional Logic**: Complex decision trees
- **File I/O**: Data persistence and retrieval
- **Error Handling**: Robust application design
- **User Interface**: Interactive console applications

## 🔮 Future Enhancements

- **Machine Learning Integration**: More sophisticated NLP
- **Database Storage**: Persistent conversation history
- **Multi-language Support**: International conversations  
- **API Integration**: External knowledge sources
- **GUI Interface**: Visual chat application
- **Real-time Chat**: Network-based messaging

## 🏆 Use Cases

- **Customer Support**: Automated first-line responses
- **Personal Assistant**: Quick information and help
- **Educational Tool**: Learning conversation patterns
- **Chatbot Foundation**: Base for advanced bots
