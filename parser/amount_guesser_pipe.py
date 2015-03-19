import contract_parser 
import sys
import csv


def parsed_to_json(parsed, doc_cloud_id, original):
    output = {}
    types_of_stuff = set([i[1] for i in parsed])
    for ty in types_of_stuff:
        output[ty] = [i[0] for i in parsed if i[1] == ty]
    output['id'] = doc_cloud_id
    output['original'] = original
    return output

if __name__ == "__main__":
    for line in sys.stdin:
        for row in csv.reader([line]):
            parsed = contract_parser.parse(row[0])
            print parsed_to_json(parsed, row[1], row[0])