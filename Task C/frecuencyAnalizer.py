class FrequencyAnalyzer:
    # This class has the responsibility to provide a method that returns a dictionary such as
    # {"word" : "timesItAppears"} with the top 10 most used words in the text

    def __init__(self, wordDictionary: dict):
        self.wordDictionary = wordDictionary

    def getTopTen(self) -> list:
        # This is a tricky sort, it took me some time to write it
        # We first convert the dictionary into a tuple list with .items()
        # Then we will compare the actual element with the next one, with key=lambda x: x[1]
        # And finally we will order it in reverse mode, in this way we will have the top ten
        sorted_words = sorted(self.wordDictionary.items(), key=lambda x: x[1], reverse=True)
        return sorted_words[:10]