"""
AI AutoReply Bot - Advanced Chat Automation
================
Features:
- Real-time chat monitoring using screen automation
- OpenAI GPT integration for intelligent responses
- Automatic message detection and reply
- Screen coordinate detection and interaction
- Clipboard operations for message handling
- Advanced chat history analysis

"""

import pyautogui
import time
import pyperclip
from openai import OpenAI

# Configuration
OPENAI_API_KEY = "<Your Key Here>"

# Screen coordinates (you need to adjust these for your screen)
CHROME_ICON = (1639, 1412)
CHAT_SELECT_START = (972, 202)
CHAT_SELECT_END = (2213, 1278)
MESSAGE_BOX = (1808, 1328)
CLICK_POSITION = (1994, 281)

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def get_screen_coordinates():
    """Helper function to get current mouse coordinates """
    print("Move mouse to desired position and press Ctrl+C to get coordinates")
    print("Press Ctrl+Break to stop")
    
    while True:
        try:
            position = pyautogui.position()
            print(f"Current position: {position}")
            time.sleep(1)
        except KeyboardInterrupt:
            break

def is_last_message_from_sender(chat_log, sender_name="Rohan Das"):
    """
    Check if the last message in chat log is from specified sender
    """
    # Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

def generate_ai_response(chat_history):
    """Generate intelligent response using OpenAI GPT"""
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a person named Naruto who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)"},
                {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] Rohan Das: "},
                {"role": "user", "content": chat_history}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Sorry, having technical difficulties! 🤖 Error: {str(e)[:50]}..."

def send_message(message):
    """Send message through chat interface"""
    # Copy message to clipboard
    pyperclip.copy(message)
    
    # Click on message box
    pyautogui.click(MESSAGE_BOX)
    time.sleep(1)
    
    # Paste the message
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    
    # Press Enter to send
    pyautogui.press('enter')
    print(f"✅ Sent: {message}")

def capture_chat_history():
    """Capture chat history from screen"""
    # Drag to select chat text
    pyautogui.moveTo(CHAT_SELECT_START)
    pyautogui.dragTo(CHAT_SELECT_END, duration=2.0, button='left')
    
    # Copy selected text
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)
    pyautogui.click(CLICK_POSITION)
    
    # Get text from clipboard
    chat_history = pyperclip.paste()
    return chat_history

def main_bot():
    """Main bot function"""
    print("🤖 AI AutoReply Bot Starting...")
    print("=" * 50)

    # Click on Chrome icon to focus
    print("Focusing on browser...")
    pyautogui.click(CHROME_ICON)
    time.sleep(1)
    
    print("🚀 Bot is now active! Monitoring chat...")
    print("Press Ctrl+C to stop the bot")
    
    while True:
        try:
            time.sleep(5)  # Check every 5 seconds
            
            # Capture current chat history
            chat_history = capture_chat_history()
            
            print("📱 Checking for new messages...")
            print(f"Last few characters: ...{chat_history[-100:]}")
            
            # Check if last message is from sender (not us)
            if is_last_message_from_sender(chat_history):
                print("🔔 New message detected! Generating response...")
                
                # Generate AI response
                response = generate_ai_response(chat_history)
                print(f"🤖 Generated response: {response}")
                
                # Send the response
                send_message(response)
                
                # Wait a bit before next check
                time.sleep(10)
            
        except KeyboardInterrupt:
            print("\n🛑 Bot stopped by user")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            time.sleep(5)

def setup_coordinates():
    """Helper to set up screen coordinates"""
    print("🔧 Screen Coordinate Setup")
    print("=" * 30)
    print("This helps you find the correct coordinates for your screen")
    print("Current coordinates in use:")
    print(f"Chrome Icon: {CHROME_ICON}")
    print(f"Chat Selection: {CHAT_SELECT_START} to {CHAT_SELECT_END}")
    print(f"Message Box: {MESSAGE_BOX}")
    print("\nTo get new coordinates, run the coordinate detector:")
    
    choice = input("Run coordinate detector? (y/n): ")
    if choice.lower() == 'y':
        get_screen_coordinates()

def test_openai():
    """Test OpenAI integration"""
    print("🧪 Testing OpenAI Integration...")
    
    test_command = '''
[20:30, 12/6/2024] Naruto: jo sunke coding ho sake?
[20:30, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:30, 12/6/2024] Rohan Das: ye
[20:30, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=DzmG-4-OASQ
[20:31, 12/6/2024] Naruto: This is hindi
[20:31, 12/6/2024] Naruto: send me some english songs
[20:31, 12/6/2024] Naruto: but wait
[20:31, 12/6/2024] Naruto: this song is amazing
[20:31, 12/6/2024] Naruto: so I will stick to it
[20:31, 12/6/2024] Naruto: send me some english song also
[20:31, 12/6/2024] Rohan Das: hold on
[20:31, 12/6/2024] Naruto: I know what you are about to send
[20:32, 12/6/2024] Naruto: 😂😂
[20:32, 12/6/2024] Rohan Das: https://www.youtube.com/watch?v=ar-3chBG4NU
ye hindi English mix hai but best hai
[20:33, 12/6/2024] Naruto: okok
[20:33, 12/6/2024] Rohan Das: Haan
'''
    
    response = generate_ai_response(test_command)
    print(f"✅ AI Response: {response}")

if __name__ == "__main__":
    print("🤖 AI AutoReply Bot")
    print("=" * 50)
    print("Choose an option:")
    print("1. Start Auto-Reply Bot")
    print("2. Setup Screen Coordinates") 
    print("3. Test OpenAI Integration")
    print("4. Get Current Mouse Coordinates")
    
    choice = input("\nEnter choice (1-4): ")
    
    if choice == "1":
        if OPENAI_API_KEY == "<Your Key Here>":
            print("⚠️  Please set your OpenAI API key first!")
        else:
            main_bot()
    elif choice == "2":
        setup_coordinates()
    elif choice == "3":
        test_openai()
    elif choice == "4":
        get_screen_coordinates()
    else:
        print("Invalid choice!")