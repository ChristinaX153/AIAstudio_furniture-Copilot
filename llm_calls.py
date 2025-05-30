from server.config import client, completion_model


def extract_activities(natural_text):
    response = client.chat.completions.create(
        model=completion_model,
        messages=[
            {
                "role": "system",
                "content": """
You are an assistant that extracts daily activities and time slots from a person's schedule.
From the user's text, extract a list in this JSON format:
[
  {"activity": "activity_name", "hours": [hour1, hour2, ...]},
  ...
]
Rules:
- Use 24-hour time (0–23)
- For hour ranges, include all full hours in between
- For vague times like 'morning' or 'evening', use typical hours (morning=7-11, evening=18-21)
- Do not explain. Only output valid JSON.
""",
            },
            {
                "role": "user",
                "content": natural_text,
            },
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content
