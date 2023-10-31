from flask import Flask, request, jsonify
import openai

app = Flask(__name__, static_folder='../frontend')

openai.api_key = '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'

@app.route('/')
def index():
    return open("/Users/yaroslav/Desktop/chatgpt_interface/index.html").read()


@app.route('/ask', methods=['POST'])
def ask_bot():
    user_message = request.json.get('message', '')
    response = openai.Completion.create(engine="davinci", prompt=user_message, max_tokens=150)
    bot_message = response.choices[0].text.strip()
    return jsonify({"message": bot_message})

if __name__ == "__main__":
    app.run(debug=True)
