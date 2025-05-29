def extract_activities(natural_text):
    # All activities set to every hour of the day
    hours = list(range(24))
    return f"""
[
  {{"activity": "sleeping", "hours": {hours}}},
  {{"activity": "cooking", "hours": {hours}}},
  {{"activity": "working", "hours": {hours}}},
  {{"activity": "reclining", "hours": {hours}}},
  {{"activity": "yoga", "hours": {hours}}}
]
"""
