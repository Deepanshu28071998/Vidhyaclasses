# Chatbot_2_2.py.

# from flask import Flask, request, jsonify
# from Chatbot_2_2 import get_bot_response  # Assuming get_bot_response is the chatbot logic

# app = Flask(__name__)

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json.get("message")
#     bot_reply = get_bot_response(user_message)
#     return jsonify({"reply": bot_reply})

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
import Chatbot_2_2

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message')
    bot_response = Chatbot_2_2.get_response(user_message)
    return jsonify(response=bot_response)

if __name__ == '__main__':
    app.run(debug=True)


