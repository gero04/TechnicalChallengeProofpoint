from fileReader import FileReader
from textProcessor import textProcessor
from wordCounter import WordCounter
from frecuencyAnalizer import FrequencyAnalyzer
from reportGenerator import ReportGenerator
import sys


def main(inputPath: str, outputDir: str):

    reportPath = f"{outputDir}/report.md"

    raw = FileReader(inputPath).readFile()
    clean = textProcessor(raw)
    counts = WordCounter(clean).countWords()
    totalWords = sum(counts.values())
    top10 = FrequencyAnalyzer(counts).getTopTen()
    report = ReportGenerator(reportPath)
    report.generateReport(top10, totalWords)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input.csv> [output_dir]")
        sys.exit(1)

    inputFile = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    main(inputFile, output_dir)