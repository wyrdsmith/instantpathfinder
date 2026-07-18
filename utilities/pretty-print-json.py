import json;

data = json.load(open('../data/classes.json',encoding='utf-8'));

json.dump(data,open('../data/classes.json','w',encoding='utf-8'),indent=2)