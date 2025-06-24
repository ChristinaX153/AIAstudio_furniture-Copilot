from flask import Flask, request, jsonify
from server.config import *
from llm_calls import extract_activities

app = Flask(__name__)

@app.route('/extract_activities', methods=['POST'])
def api_extract_activities():
    data = request.get_json()
    prompt = data.get("prompt", "")
    print("Received prompt:", prompt)

    try:
        result = extract_activities(prompt)
        print("Extracted result:", result)
    except Exception as e:
        print("Error during extraction:", e)
        result = {
            "activities_json": [],
            "hourly_metabolic_rates": [],
            "hourly_activities": [],
            "hourly_furniture": []
        }

    return jsonify({
        "activities_json": result.get("activities_json", []),
        "hourly_metabolic_rates": result.get("hourly_metabolic_rates", []),
        "hourly_activities": result.get("hourly_activities", []),
        "hourly_furniture": result.get("hourly_furniture", [])
    })

if __name__ == '__main__':
    app.run(debug=True, port=5050)
