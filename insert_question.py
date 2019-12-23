import json
from mongodb_models import Mongo

with open("dataset/MilitaryCorpus.json","r") as f:
    data = json.load(f)
    client = Mongo().connectDB()
    col = client["questions_data"]
    for news in data:
        questions = news["questions"]
        for question in questions:
            col.insert_one(question)
            print(question)
