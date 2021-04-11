import os
from document_test import TreatDoc


paths = []
fileFormat = ("docx", "txt")
for root, dirs, files in os.walk("C:/Users/Виталий/Desktop/Мага 2 семестр"):
    for file in files:
        if file.endswith(fileFormat) and not file.startswith('~'):
            paths.append(os.path.join(root, file))
            f = TreatDoc(file, os.path.join(root, file))
            name = f.name()
            text = f.text()
            #print(name)
            #print(text)

#for i in paths:
#    print(i)

from nltk.stem import SnowballStemmer

snowball = SnowballStemmer(language="english")
print(snowball.stem("found"))

import nltk
nltk.download('stopwords')

