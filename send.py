from groupy import Client
import os
import random

GROUP_ID = 57653465
MESSAGES = [
    "Good morning",
    "good morning",
    "good morning brothers",
    "Hello brothers good morning",
    "goodmorning",
    "Goodmorning",
    "Good morning to all the brothers",
]

token = os.environ["GROUPME_ACCESS_TOKEN"]
if not token:
    with open(os.environ["HOME"] + "/groupme_token.txt", "r") as f:
        token = f.read().strip()

client = Client.from_token(token)
group = client.groups.get(id=GROUP_ID)
group.post(text=random.choice(MESSAGES))
