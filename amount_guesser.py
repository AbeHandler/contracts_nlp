import contract_parser 
import sys
import csv


with open(sys.argv[1], 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in spamreader:
            parsed = contract_parser.parse(row[0])
            agreement_amount = [i[0] for i in parsed if i[1]=="agreement_amount"]
            if len(agreement_amount) > 0:
                print "".join(agreement_amount), row[1], row[0]