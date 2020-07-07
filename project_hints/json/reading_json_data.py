import json

with open("data/quiz.json") as json_file:
    json_data = json.load(json_file)

# print(json_data["quiz"]["One"]["question"])

for key, value in json_data["quiz"].items():
    print(f"Question {key}: {value['question']}")
    # print(f"{value['question']}")
    for option in value['options']:
        print(f"      {option}")