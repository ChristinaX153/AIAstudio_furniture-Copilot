from flask import Flask, request, jsonify
from llm_calls import extract_activities

app = Flask(__name__)

@app.route('/extract_activities', methods=['POST'])
def api_extract_activities():
    data = request.get_json()
    prompt = data.get("prompt", "")
    result = extract_activities(prompt)
    return jsonify({"activities": result})

if __name__ == '__main__':
    app.run(debug=True)
