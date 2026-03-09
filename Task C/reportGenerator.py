class ReportGenerator:
    # This class has the responsibility to create a report to inform the frequency of the words we analyzed

    def __init__(self, reportPath: str):
        self.reportPath = reportPath
    
    def generateReport(self, topTen: list, totalWords: int):
        content = f"""# Text Frequency Analysis
## Technical Challenge Intern Program - Proofpoint - March 2026
### Word Statistics (Total words: {totalWords})
- 1st word: "{topTen[0][0]}", {topTen[0][1]} times ({topTen[0][1]/totalWords*100:.2f}%)
- 2nd word: "{topTen[1][0]}", {topTen[1][1]} times ({topTen[1][1]/totalWords*100:.2f}%)
- 3rd word: "{topTen[2][0]}", {topTen[2][1]} times ({topTen[2][1]/totalWords*100:.2f}%)
- 4th word: "{topTen[3][0]}", {topTen[3][1]} times ({topTen[3][1]/totalWords*100:.2f}%)
- 5th word: "{topTen[4][0]}", {topTen[4][1]} times ({topTen[4][1]/totalWords*100:.2f}%)
- 6th word: "{topTen[5][0]}", {topTen[5][1]} times ({topTen[5][1]/totalWords*100:.2f}%)
- 7th word: "{topTen[6][0]}", {topTen[6][1]} times ({topTen[6][1]/totalWords*100:.2f}%)
- 8th word: "{topTen[7][0]}", {topTen[7][1]} times ({topTen[7][1]/totalWords*100:.2f}%)
- 9th word: "{topTen[8][0]}", {topTen[8][1]} times ({topTen[8][1]/totalWords*100:.2f}%)
- 10th word: "{topTen[9][0]}", {topTen[9][1]} times ({topTen[9][1]/totalWords*100:.2f}%)
"""
        with open(self.reportPath, 'w') as report:
            report.write(content)
            