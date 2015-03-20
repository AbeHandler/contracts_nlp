import json
import ast
import re
from colorama import Fore, Back, Style
import csv

def filter_hits(hits, filter_term):
    hits = [ast.literal_eval(h) for h in hits]
    hits = [h for h in hits if filter_term in h.keys()]
    return hits


def color_me_red(input_text, color_this):
    return input_text.replace(color_this, Fore.RED + color_this + Fore.RESET)

def write_new(line):
    with open('corrected.csv', 'a') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow([line])


data_file = "".join([p for p in open("parsed.json")])

hits = re.findall("{[^}]+}", data_file)

hits = filter_hits(hits, "agreement_amount")

counter = 0

for h in hits:
    counter += 1
    print str(counter) + " of " + str(len(hits))
    print "{} | {}".format(color_me_red(h['agreement_amount'][0], h['agreement_amount'][0]), color_me_red(h['original'].strip(), h['agreement_amount'][0]))
    var = raw_input("Correct (c) or Not (n)?")
    if var == "n":
        write_new(h['original'])