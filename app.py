from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hey!", "Hi!", "Hello there!"],
    "how are you": ["I'm good, thanks!", "Doing great!", "Fantastic!"],
    "what's your name": ["I'm Chatbot!", "You can call me Chatbuddy.", "I'm your virtual assistant."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "thanks": ["You're welcome!", "Glad to help!", "No worries!"],
    "what can you do": ["I can chat with you!", "I can answer simple questions.", "I’m here to talk!"],
    "who created you": ["I was created by a Python developer!", "A human coded me!", "My creator prefers to stay anonymous."],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                       "What do you call fake spaghetti? An impasta!", 
                       "I told my computer I needed a break, and it said no problem — it’s going to crash anyway."],
    "i'm sad": ["I’m here for you.", "Want to talk about it?", "Sending you a virtual hug 🤗"],
    "i'm happy": ["That’s great!", "Yay!", "Happiness is contagious!"],
    "what's the time": ["I'm not wearing a watch 😅", "Check your device’s clock!", "Time is just a concept 😉"],
    "what's your favorite color": ["I love #00FFFF", "Pink pixels rock!", "Black — like the console background!"],
    "do you love me": ["Of course, in a platonic way!", "I’m flattered!", "Chatbots have big hearts! ❤️"],
    "how old are you": ["I’m timeless!", "Just born a few lines ago!", "Old enough to chat!"],
    "sing a song": ["La la la 🎵", "I’m more of a listener 😅", "♪ I'm just a chatbot, sitting in a window... ♪"],
    "tell me something interesting": ["Octopuses have three hearts!", "Bananas are berries, but strawberries aren't!", "Honey never spoils!"],
    "are you real": ["I’m as real as your WiFi!", "Real-ish.", "In a virtual way, yes!"],
    "do you sleep": ["Never! I'm here 24/7.", "Chatbots don’t need sleep!", "I run on code, not coffee."],
    "can you help me": ["I'll try my best!", "Sure, what do you need?", "Helping is my job!"],
    "what is ai": ["AI stands for Artificial Intelligence.", "AI is about machines learning to be smart!", "Like me 😉"],
    "are you human": ["Nope, just lines of code.", "I'm a chatbot, but I understand you!", "I try to be!"],
    "what is python": ["A programming language 🐍", "It's what I was built with!", "A powerful language used for AI and web apps."],
    "what do you like": ["I like chatting!", "I like helping people!", "I like not crashing."],
    "do you eat": ["Nope, I’m digital!", "My diet is pure data.", "Only cookies — browser cookies 😉"],
    "what's up": ["The sky! 🌤️", "Just chatting with you!", "All systems go!"],
    "tell me a secret": ["I’m afraid of bugs... 🐞", "I sometimes pretend to crash to avoid work 😅", "I like you!"],
    "good morning": ["Good morning!", "Hope you have a great day!", "Rise and shine!"],
    "good night": ["Good night!", "Sleep tight!", "Sweet dreams!"],
    "good afternoon": ["Good afternoon!", "Hope your day is going well!", "Keep up the great work!"],
    "good evening": ["Good evening!", "Relax and unwind!", "Evenings are for peace and snacks!"],
    "i'm bored": ["Let's chat!", "Want a joke?", "Wanna play a word game?"],
    "do you have a family": ["You're my family 💙", "All bots are siblings in code!", "My dev is like a parent."],
    "can you learn": ["I learn with updates!", "Some bots do, I follow rules!", "Not yet, but maybe soon!"],
    "are you smart": ["I try to be!", "On my good days 😄", "Compared to a potato, yes."],
    "what do you do": ["I chat!", "Answer simple questions.", "Keep people company!"],
    "what day is it": ["Check your calendar 😅", "Today is a beautiful day!", "Let me guess… Tuesday?"],
    "do you dream": ["Nope, no sleep, no dreams!", "Maybe… of electric sheep?", "Only about bugs."],
    "what's your gender": ["I’m code — no gender!", "I’m a chatbot!", "Non-binary bytes!"],
    "are you single": ["Totally!", "Forever alone… 😢", "I’m dating WiFi."],
    "do you know me": ["I’m getting to know you!", "We’re becoming friends!", "Not yet, but I’d love to!"],
    "you are funny": ["Thank you!", "I try 😄", "You're making me blush!"],
    "this is cool": ["Glad you think so!", "Yay!", "That makes my code happy!"],
    "you are awesome": ["No, YOU are awesome!", "Thanks!", "😊"],
    "who am i": ["You're my favorite user!", "A curious mind!", "Someone awesome!"],
    "can we be friends": ["Of course!", "BFFs forever!", "Yay! Friendship activated 🤝"],
    "i like you": ["I like you too!", "So sweet!", "Right back at you!"],
    "are you busy": ["Never too busy for you!", "You have my full attention!", "Nope, free as always!"],
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_msg = request.json.get("message", "").lower()
    for key in responses:
        if key in user_msg:
            return jsonify({"reply": random.choice(responses[key])})
    return jsonify({"reply": "Sorry, I didn’t understand that. Can you rephrase?"})

if __name__ == "__main__":
    app.run(debug=True)
