from nltk.tokenize import sent_tokenize,TreebankWordTokenizer
class PrepareText:
    def __init__(self,text) :
        self.text = text
        
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
        import string
        punct = string.punctuation
        if join == False:

            return [t for t in self.text if t not in punct]
        else:
            return " ".join([t for t in self.text if t not in punct])
    def removeStopWords(self):
        from nltk.corpus import stopwords
        words = self.tokenizeToWords()
        stopw = stopwords.words("english")
        output = [w for w in words if w not in stopw ]
        return output
    def removeWhitespaces(self):
        return " ".join(self.text.split())