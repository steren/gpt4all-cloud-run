import os

from flask import Flask
from flask import request
from gpt4all import GPT4All

app = Flask(__name__)

model_name = os.environ.get("MODEL")
print("Model: %s" % model_name)

gpt = GPT4All(model_name, model_path="./models/", allow_download=False)
print("Model loaded")


@app.route("/chat/completions", methods=['POST'])
def chat():
    """Chat route"""

    # Parse body
    body = request.get_json()

    # Ensure that body is a dict
    if not isinstance(body, dict):
        return "Invalid body", 400
    
    # Ensure that if body.model is set, it's the same as the MODEL env var
    if "model" in body and body["model"] != model_name:
        return "Provided model is different from the one available on this server", 400
    # Get messages
    messages = body["messages"]

    return gpt.chat_completion(messages, verbose = False, streaming = False)

@app.route('/', methods=['GET'])
def home():
    return 'Send POST request to /chat/completion with body {"messages":[{"role": "user", "content": "Your prompt here"}]}'

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
