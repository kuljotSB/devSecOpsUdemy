from flask import Flask, request, jsonify
from src import chatCompletionsAPI

app = Flask(__name__)

@app.route("/chat", methods = ['POST'])
def chat():
    data = request.get_json()
    chat_response = chatCompletionsAPI.chat_completions_api(data.get('user_query'))
    return jsonify({"response": chat_response})

if __name__ == '__main__':
    app.run(debug=True)
    