import json
import ast
import re

data_file = "".join([p for p in open("parsed.json")])

hits = re.findall("{[^}]+}", data_file)

for h in hits:
    h = ast.literal_eval(h)
    print h.keys()