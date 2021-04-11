from collections import Counter
from dataclasses import dataclass
from langdetect import detect

from .analysis import analyze_ru, analyze_en


@dataclass
class Abstract:
    """Document abstarct"""
    ID: int
    title: str
    text: str
    path: str

    @property
    def fulltext(self):
        return ''.join([self.title, self.text])

    def analyze_ru(self):
        self.term_frequencies = Counter(analyze_ru(self.fulltext))

    def analyze_en(self):
        self.term_frequencies = Counter(analyze_en(self.fulltext))

    def term_frequency(self, term):
        return self.term_frequencies.get(term, 0)