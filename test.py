import json, ast

f = open('champion.json')
data = json.load(f)
f.close()

champion_dict = {}

for (k, v) in data["data"].items():
    champion_dict[v["key"]] = k

del champion_dict["62"]

champion_dict["62"] = 'Wukong'

print(ast.literal_eval(json.dumps(champion_dict)))
