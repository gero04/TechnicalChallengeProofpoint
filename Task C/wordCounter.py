import string
class WordCounter:
    # This class returns a dictionary with words as keys and the number of times they appear

    def __init__(self, cleanText: str):
        self.wordList = cleanText.split()
        self.wordDictionary = {}
    
    def countWords(self) -> dict:
        for word in self.wordList:
            if word in self.wordDictionary:
                self.wordDictionary[word] += 1
            else:
                self.wordDictionary[word] = 1
        return self.wordDictionary
