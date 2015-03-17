import contract_parser 
import sys
import csv

if __name__ == "__main__":
    for line in sys.stdin:
        row = line.split(",")
        parsed = contract_parser.parse(row[0])
        agreement_amount = [i[0] for i in parsed if i[1]=="agreement_amount"]
        print line
        if len(agreement_amount) > 1:
            print "".join(agreement_amount), row[1], row[0]