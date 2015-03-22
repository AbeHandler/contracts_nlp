import json
import ast
import re
from colorama import Fore, Back, Style
import csv
import sys

tag_to_check = sys.argv[1]

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

hits = filter_hits(hits, tag_to_check)

counter = 0

for h in hits:
    counter += 1
    print str(counter) + " of " + str(len(hits))
    print "{} | {}".format(color_me_red(h[tag_to_check][0], h[tag_to_check][0]), color_me_red(h['original'].strip(), h[tag_to_check][0]))
    var = raw_input("Correct (c) or Not (n)?")
    if var == "n":
        write_new(h['original'])