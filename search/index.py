import math

from langdetect import detect

from .timing import timing
from .analysis import analyze_ru


class Index:
    def __init__(self):
        self.index = {}
        self.documents = {}

    def index_document(self, document):
        if document.ID not in self.documents:
            self.documents[document.ID] = document
            if detect(document.text) == "ru":
                document.analyze_ru()
            """elif detect(document.text) == "en":
                document.analyze_en()"""

        if detect(document.text) == "ru":
            for token in analyze_ru(document.fulltext):
                if token not in self.index:
                    self.index[token] = set()
                self.index[token].add(document.ID)
        """elif detect(document.text) == "en":
            for token in analyze_en(document.fulltext):
                if token not in self.index:
                    self.index[token] = set()
                self.index[token].add(document.ID)"""

    def document_frequency(self, token):
        return len(self.index.get(token, set()))

    def inverse_document_frequency(self, token):
        return math.log10(len(self.documents) / self.document_frequency(token))

    def _results(self, analyzed_query):
        return [self.index.get(token, set()) for token in analyzed_query]

    @timing
    def search(self, query, search_type='AND', rank=False):
        if search_type not in ('AND', 'OR'):
            return []

        #if detect(query) == "ru":
        analyzed_query = analyze_ru(query)
        """elif detect(query) == "en":
            analyzed_query = analyze_en(query)"""

        results = self._results(analyzed_query)
        if search_type == 'AND':
            documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]
            return documents
        if search_type == 'OR':
            documents = [self.documents[doc_id] for doc_id in set.union(*results)]
            return documents
        if rank and search_type == 'AND':
            documents = [self.documents[doc_id] for doc_id in set.intersection(*results)]
            return self.rank(analyzed_query, documents)
        if rank and search_type == 'OR':
            documents = [self.documents[doc_id] for doc_id in set.union(*results)]
            return self.rank(analyzed_query, documents)

    def rank(self, analyzed_query, documents):
        results = []
        if not documents:
            return results
        for document in documents:
            score = 0.0
            for token in analyzed_query:
                tf = document.term_frequency(token)
                idf = self.inverse_document_frequency(token)
                score += tf * idf
            results.append((document, score))
        return sorted(results, key=lambda doc: doc[1], reverse=True)