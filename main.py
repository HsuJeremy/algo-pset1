import json
import pandas as pd
import matplotlib.pyplot as plt

with open("responses.json") as file:
    data = json.load(file)

list_data = [i for i in data.values()]


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
    f_score = (person1["f"] + person2["f"]) / 2

    return gender_score * year_score * abs(1 / (question_score / 100 - f_score + 1))


# print(score(data["2"], data["3"]))

pair = []
# If want to plot non-zero pairs
for person1 in data:
    for person2 in data:
        if person1 < person2:
            scr = score(data[person1], data[person2])
            if scr != 0:
                pair.append(scr)


# If want to plot all pairs
# for person1 in data:
#     for person2 in data:
#         if person1 < person2:
#             pair.append(score(data[person1], data[person2]))

# print(len(pair))

# Create dataframe of pair list
df = pd.DataFrame(pair, columns=['Score'])

# matplotlib histogram
plt.hist(df['Score'], color='blue', edgecolor='black', bins=int(180 / 5))

# Add labels
plt.title('Histogram of Pair Scores')
plt.xlabel('Scores')
plt.ylabel('Count')

plt.show()
