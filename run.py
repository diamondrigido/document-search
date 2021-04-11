import os.path

from load import load_documents
from search.timing import timing
from search.index import Index


@timing
def index_documents(documents, index):
    for i, document in enumerate(documents):
        index.index_document(document)
        if i % 5000 == 0:
            print(f'Indexed {i} documents', end='\r')
    return index


if __name__ == '__main__':
    index = index_documents(load_documents(), Index())
    print(f'Index contains {len(index.documents)} documents')

    index.search('дата', search_type='AND')
    index.search('дата', search_type='OR')
    index.search('дата', search_type='AND', rank=True)
    index.search('дата', search_type='OR', rank=True)