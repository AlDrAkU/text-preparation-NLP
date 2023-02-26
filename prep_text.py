import nltk
from nltk.tokenize import sent_tokenize,TreebankWordTokenizer
from nltk.corpus import stopwords
from string import punctuation
nltk.download("punkt")
nltk.download("stopwords")
class PrepareText:
    def __init__(self,text) :
        self.text = text
        self.punct = punctuation
        self.stopw = stopwords.words("english")
        
    def lowercaseText(self):
        return str.lower(self.text)

    def tokenizeToSentence(self):
        return sent_tokenize(self.text)
    def tokenizeToWords(self):
   
        return TreebankWordTokenizer().tokenize(self.text)
    def removeNumbers(self):
        import re
        return re.sub(r'\d+','',self.text)
    def removePunctuation(self,join=False):
        if not isinstance(self.text,list):
            self.text = self.tokenizeToWords()

        if join == False:

            return [t for t in self.text if t not in self.punct]
        else:
            return " ".join([t for t in self.text if t not in self.punct])
    def removeStopWords(self):

        words = self.tokenizeToWords()

        output = [w for w in words if w not in self.stopw ]
        return output
    def removeWhitespaces(self):
        return " ".join(self.text.split())