class FileReader:
    # This class has the responsibility to read a file (.txt) and return a raw string with all its content

    def __init__(self, inputPath: str):
        self.inputPath = inputPath

    def readFile(self) -> str:
        with open(self.inputPath, 'r', encoding='utf-8') as textFile:
            return textFile.read()