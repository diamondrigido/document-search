import docx


class TreatDoc(object):
    def text(self):
        if self.pathFile.endswith("docx") or self.pathFile.endswith("doc"):
            return self.ms_word()
        elif self.pathFile.endswith("csv") or self.pathFile.endswith("txt"):
            return self.txt_csv_format()

    def __init__(self, title, pathfile):
        self.title = title
        self.pathFile = pathfile

    def name(self):
        if self.title.endswith("docx"):
            return self.title.replace("docx", "")
        elif self.title.endswith("csv"):
            return self.title.replace("csv", "")
        elif self.title.endswith("txt"):
            return self.title.replace("txt", "")

    def ms_word(self):
        doc = docx.Document(self.pathFile)
        text = []
        for paragraph in doc.paragraphs:
            text.append(paragraph.text)
        text = "\n".join(text)
        return text

    def txt_csv_format(self):
        f = open(self.pathFile, "r")
        text = f.read()
        return text
