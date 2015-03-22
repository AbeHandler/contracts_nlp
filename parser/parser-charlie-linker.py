import csv
import re
import os 

from collections import Counter
from utilities import filter_hits
from utilities import get_page_with_phrase


data_file = "".join([p for p in open("parsed.json")])

hits = re.findall("{[^}]+}", data_file)

hits = filter_hits(hits, 'agreement_amount')

output = []

for h in hits:
	output.append((h['id'], h['original'], h['agreement_amount']))

ids = [o[0] for o in output]

counter = Counter(ids)

to_check_with_human = []
to_retrain = []

for c in counter.keys():
    if int(counter[c]) == 1:
        to_check_with_human.append(c)
    if int(counter[c]) > 1:
        to_retrain.append(c)

try:
    os.remove("charlie_queue.csv")
except:
	pass 

for i in to_check_with_human:
    check_w_charlie = [o for o in output if o[0]==i]
    assert len(check_w_charlie) == 1
    check_w_charlie = check_w_charlie.pop()
    dcid = check_w_charlie[0]
    context = check_w_charlie[1]
    amt = check_w_charlie[2].pop()
    page_in_dc = str(get_page_with_phrase(dcid, context))
    with open('charlie_queue.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerows([dcid, context,amt,page_in_dc])