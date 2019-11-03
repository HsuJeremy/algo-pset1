import json 

with open("responses.json") as file:
	data = json.load(file)

# Each JSON entry (i.e. person) is a dictionary
# Calculate compatibility score for two people
def score(person1, person2): 
	# Assign each question an arbitrary weight of 10 for now 
	weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
	# Find the question similarity score
	question_score = 0
	for i in range(len(person1["answers"])):
		if person1["answers"] == person2["answers"]: 
			question_score += weights[i] * 1
		else: 
			question_score += weights[i] * 0.20

	# Year compatibility
	year_score = 1 / (abs(person1["year"] - person2["year"]) + 1)

	# Gender preference compatiblity 
	gender_score = 0
	if person1["gender"] in person2["gender_preferences"] and person2["gender"] in person1["gender_preferences"]:
		gender_score = 1

	# Similarity preference compatibility
	f_score = person1["f"] + person2["f"] / 2

	return gender_score * year_score * abs(1 / (question_score / 100 - f_score + 1))

print(score(data["0"], data["13"]))
