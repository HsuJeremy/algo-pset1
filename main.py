import json 

with open("responses.json") as file:
	data = json.load(file)

print(data)