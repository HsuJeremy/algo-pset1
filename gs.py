import json
from main import score

with open("responses.json") as file:
    data = json.load(file)

d1 = dict(list(data.items())[:len(data)//2])
d2 = dict(list(data.items())[len(data)//2:])

propscrDict = {}
const1 = 0
const2 = 0
while len(d1) != 0 and len(d2) != 0:
    scoreDict = {}
    for men in d2:
        scoreDict[men] = []

        for women in d1:
            value = score(d2[men], d1[women])
            if value > 0:
                scoreDict[men].append((women, value))

        scoreDict[men].sort(key=lambda x: x[1], reverse=True)

    for proposer in scoreDict:
        if len(scoreDict[proposer]) == 0:
            continue
        if scoreDict[proposer][0][0] not in propscrDict.keys():
            propscrDict[scoreDict[proposer][0][0]] = (proposer, scoreDict[proposer][0][1])
        else:
            if scoreDict[proposer][0][1] > propscrDict[scoreDict[proposer][0][0]][1]:
                propscrDict[scoreDict[proposer][0][0]] = (proposer, scoreDict[proposer][0][1])

    for couple in propscrDict:
        d1.pop(couple, None)
        d2.pop(propscrDict[couple][0], None)
    if const1 == len(d1) and const2 == len(d2):
        break
    const1 = len(d1)
    const2 = len(d2)

for i in d1:
    for j in d2:
        for someone in propscrDict:
            if propscrDict[someone][0] == j and score(d1[i], d2[j]) > propscrDict[j][2] and score(d1[i], d2[j]) > propscrDict[someone][1]:
                print("unstable")
