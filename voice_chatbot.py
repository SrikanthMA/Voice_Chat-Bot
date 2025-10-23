import speech_recognition as sr
import pyttsx3
import random

# Initialize speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"🤖 {text}")
    engine.say(text)
    engine.runAndWait()

def get_bot_response(user_input):
    text = user_input.lower()

    if "hello" in text or "hi" in text:
        return "Hey there! How's your day going?"
    elif "sad" in text or "upset" in text or "depressed" in text:
        return "I'm really sorry you're feeling that way. Want to talk about what's bothering you?"
    elif "happy" in text or "great" in text or "awesome" in text:
        return "That's wonderful to hear! What made you feel so good today?"
    elif "nothing" in text or "bored" in text:
        return "Sounds like a quiet day. Want me to tell you a fun fact or a joke?"
    else:
        fallback_responses = [
            "Thanks for sharing. Anything exciting happening today?",
            "Got it! Want to chat more about it?",
            "Interesting... tell me more!",
            "I'm here to listen. What's on your mind?"
        ]
        return random.choice(fallback_responses)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, speech service is unavailable."

# Main loop
speak("Hi Rama! I'm your voice-enabled chatbot. Say 'exit' to stop chatting.")

while True:
    user_input = listen()
    if "exit" in user_input.lower() or "quit" in user_input.lower():
        speak("Take care! Chat with you later.")
        break
    response = get_bot_response(user_input)
    speak(response)