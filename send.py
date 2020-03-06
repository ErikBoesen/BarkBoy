from groupy import Client
import os
import random

GROUP_ID = 57653465
MESSAGES = [
    "Good morning",
    "good morning",
    "good morning brothers",
    "Hello brothers good morning",
    "goodmorning 😁",
    "Good morning to all the brothers",
]


client = Client.from_token(os.environ["GROUPME_ACCESS_TOKEN"])
group = client.groups.get(id=GROUP_ID)
#group.leave()
group.post(text=random.choice(MESSAGES))
