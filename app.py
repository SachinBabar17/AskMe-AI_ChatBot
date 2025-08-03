import os
import requests
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify

load_dotenv()

app = Flask(__name__)

HF_API_URL = "https://router.huggingface.co/v1/chat/completions"
HF = os.environ.get("HF_TOKEN")
if not HF:
    raise ValueError("HF_TOKEN environment variable not set. Please set it in your .env file or environment.")

HF_HEADERS = {
    "Authorization": f"Bearer {HF}",
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    payload = {
        "messages": [
            {"role": "user", "content": user_input}
        ],
        "model": "mistralai/Mistral-7B-Instruct-v0.2:featherless-ai"
    }
    try:
        response = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload)
        response.raise_for_status()
        generated = response.json()
        # Debug print
        print("HF API response:", generated)
        if "choices" in generated and generated["choices"]:
            reply = generated["choices"][0]["message"]["content"]
        elif "error" in generated:
            reply = f"Error from model: {generated['error']}"
        else:
            reply = "Error: Unexpected response format."
    except Exception as e:
        reply = f"Error: {str(e)}"
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)