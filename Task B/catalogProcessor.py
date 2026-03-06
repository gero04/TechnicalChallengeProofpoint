from episodeParser import EpisodeParser
from duplicateDetector import DuplicateDetector
import csv

class CatalogProcessor: 
    # The responsibility of this class are:
    # 1. Read the CSV
    # 2. Parse each row with class EpisodeParser
    # 3. Detect duplicates with class DuplicateDetector
    # 4. Write the output
    # 5. Generate the report
    def __init__(self, inputPath: str, outputPath: str, reportPath: str):
        self.inputPath = inputPath
        self.outputPath = outputPath
        self.reportPath = reportPath
        self.episodeParser = EpisodeParser()
        self.duplicateDetector = DuplicateDetector()

        # This are the counters that we will be using for the output and report
        self.totalInput = 0
        self.totalOutput = 0
        self.discarded = 0
        self.corrected = 0

    def process(self):
        # Here we will be taking care of the 5 responsibilities
        
        # First, we will create a reader object, and open the CSV with it
        with open(self.inputPath, 'r') as csvFile:
            csvReader = csv.DictReader(csvFile, fieldnames=['SeriesName', 'SeasonNumber', 'EpisodeNumber', 'EpisodeTitle', 'AirDate'])

            # We get the headers of the file (SeriesName, SeasonNumber, EpisodeNumber, EpisodeTitle and AirDate)
            headers = next(csvReader)

            # We iterate through the rows, parsing them
            for rawRow in csvReader:

                # First we increment the total amount of rows
                self.totalInput += 1

                # We parse the raw row, and detect if it was (or not) corrected
                episode, wasCorrected = self.episodeParser.parse(rawRow)
                
                # If we happen to have to discard the episode we increment the counter of discarded episodes
                if episode is None: 
                    self.discarded += 1
                    continue
                
                # If we had to correct the episode we increment the counter of corrected episodes
                if wasCorrected:
                    self.corrected += 1
                
                # If our episode was unique and wasn't discarded, we add it to the unique episodes array on DuplicateDetector
                self.duplicateDetector.addOrUpdate(episode)
        
        # Now we will write the uotput file
        with open(self.outputPath, 'w', newline='') as cleanCSVfile:

            # We create the writer using a comma as a delimiter
            cleanWriter = csv.writer(cleanCSVfile, delimiter=',')

            # We write the headers
            cleanWriter.writerow(['SeriesName', 'SeasonNumber', 'EpisodeNumber', 'EpisodeTitle', 'AirDate'])

            # We write the rows with the unique episodes we have in the duplicate detector
            for cleanRow in self.duplicateDetector.getUniqueEpisodes():
                
                self.totalOutput += 1
                cleanWriter.writerow([
                    cleanRow.seriesName,
                    cleanRow.seasonNumber,
                    cleanRow.episodeNumber,
                    cleanRow.episodeTitle,
                    cleanRow.airDate
                ])
        return (self.totalInput, self.totalOutput, self.discarded, self.corrected, self.duplicateDetector.duplicatesCount)