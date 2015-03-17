import glob
import csv
import re
import glob
import nltk
import string
from nltk.corpus import words
from contracts_ml.settings import Settings

s = Settings()

glob_files = glob.glob(s.corpus_location + "/*_text.txt")

pattern = ".{75}\$[0-9]+.{75}"

output = []


def is_english(token):
    if token in words.words():
        return True
    else:
        return False


def add_line(hit, dcid):

    with open("data.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow([hit, dcid])


for f in glob_files:
    lines = "".join([l.replace("\\n", "") for l in open(f)]).replace("\\n", "")
    for hit in re.findall(pattern, lines):
        tokens = nltk.word_tokenize(hit)
        english_tokens = [t for t in tokens if is_english(t)]
        if float(len(english_tokens))/float(len(tokens)) > .5:   #if more than 50 % english...
            dcid = f.replace("_text.txt", "").replace(s.corpus_location, "").replace("/", "")
            add_line(hit, dcid)