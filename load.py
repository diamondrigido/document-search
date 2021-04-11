import os
import time

from search.treat import TreatDoc
from search.documents import Abstract


def load_documents():
    start = time.time()
    fileFormat = ("docx", "txt", "csv")
    doc_id = 0
    for root, dirs, files in os.walk("C:/Users/Виталий/Desktop/Мага 2 семестр"):
        for file in files:
            if file.endswith(fileFormat) and not file.startswith('~'):
                pathFile = os.path.join(root, file)
                f = TreatDoc(file, pathFile)
                title = f.name()
                text = f.text()
                path = pathFile

                yield Abstract(ID=doc_id, title=title, text=text, path=path)

                doc_id += 1
    end = time.time()
    print(f"Время индексирование всех файлов в выбранной директории составляет {end - start} секунд")
