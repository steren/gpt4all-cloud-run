import os

from flask import Flask
from gpt4all import GPT4All

app = Flask(__name__)

model_name = os.environ.get("MODEL")

@app.route("/")
def chat():
    """Chat route"""

    gpt = GPT4All(model_name, model_path="./models/", allow_download=False)
    messages = [{"role": "user", "content": "Name 3 colors"}]
    return gpt.chat_completion(messages)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))