import json

dt = {'b': 2, 'c': 4, 'a': 6}
s2 = json.dumps(dt, sort_keys=True, indent=6)
print(s2)
