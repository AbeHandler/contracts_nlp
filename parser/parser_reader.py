import json
import ast
import re

data_file = "".join([p for p in open("parsed.json")])

hits = re.findall("{[^}]+}", data_file)

agreement_amounts = []

for h in hits:
    h = ast.literal_eval(h)
    if "agreement_amount" in h.keys():
        agreement_amounts.append(h)

print agreement_amounts