import ast

from documentcloud import DocumentCloud
client = DocumentCloud()


def get_page_with_phrase(doc_cloud_id, phrase):
    doc = client.documents.get(doc_cloud_id)
    for p in range(1,doc.pages + 1):
        text = doc.get_page_text(p)
        #if phrase in doc.get_page_text(p):
        #    return p
    return 1


def filter_hits(hits, filter_term):
    hits = [ast.literal_eval(h) for h in hits]
    hits = [h for h in hits if filter_term in h.keys()]
    return hits