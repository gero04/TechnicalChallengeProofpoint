import string

def textProcessor(rawText: str):
    # This function will return a clean text (all lowercase, only words and spaces)
    cleanText = ""

    for character in rawText:
        if character.lower() in string.ascii_lowercase or character.lower() == " ":
            cleanText = cleanText + character.lower()
        else:
            cleanText = cleanText + " "
