import json
import ast
import re
from colorama import Fore, Back, Style


def filter_hits(hits, filter_term):
    hits = [ast.literal_eval(h) for h in hits]
    hits = [h for h in hits if filter_term in h.keys()]
    return hits


def color_me_red(input_text, color_this):
    return input_text.replace(color_this, Fore.RED + color_this + Fore.RESET)


data_file = "".join([p for p in open("parsed.json")])

hits = re.findall("{[^}]+}", data_file)

hits = filter_hits(hits, "agreement_amount")

for h in hits:
    print "{} | {}".format(color_me_red(h['agreement_amount'][0], h['agreement_amount'][0]), color_me_red(h['original'].strip(), h['agreement_amount'][0]))