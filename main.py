import os

from flask import Flask
from flask import request
from gpt4all import GPT4All

app = Flask(__name__)

model_name = os.environ.get("MODEL")
print("Model: %s" % model_name)

gpt = GPT4All(model_name, model_path="./models/", allow_download=False)
print("Model loaded")


@app.route("/")
def chat():
    """Chat route"""

    prompt = request.args.get('prompt', default = "Hello", type = str)

    messages = [{"role": "user", "content": prompt}]
    return gpt.chat_completion(messages)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
