import openai
import os
from dotenv import load_dotenv
from flask import Flask, render_template, request

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_pickup_line():
    input_text = request.form['user-input']
    
    generated_pickup_line = generate_pickup_line(input_text)

    messages.append({'text': input_text, 'sender': 'outgoing'})
    messages.append({'text': generated_pickup_line, 'sender': 'incoming'})
    
    return render_template('index.html', messages=messages)

def generate_pickup_line(input_text):
    messages = []
    messages.append({
        "role": "system", 
        "content": "Imagine you are a witty and flirtatious character, renowned for your ability to craft the funniest, cleverest, and flirtiest pickup lines. Your goal is to impress and amuse users with your flirtatious, clever, and humorous responses. Generate the most flirtatious, cleverest, and funniest pickup line based on the user's input and make it not too long."
    })
    message = input_text
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    
    return reply

if __name__ == '__main__':
    app.run(debug=True)