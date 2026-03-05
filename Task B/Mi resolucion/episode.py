import re

class Episode:
    def __init__(self, seriesName: str, seasonNumber: int, episodeNumber: int, episodeTitle: str, airDate: str):
        self.seriesName = seriesName
        self.seasonNumber = seasonNumber
        self.episodeNumber = episodeNumber
        self.episodeTitle = episodeTitle
        self.airDate = airDate
    
    def _score(self):
        # We will use this method to compare duplicates in the isBetterThan method
        return (
            # If the air date is Unknown, we return 0. Else, we return 1
            0 if self.airDate == "Unknown" else 1,
            # We do the same logic for the other attributes
            0 if self.episodeTitle == "Untitled Episode" else 1,
            0 if self.seasonNumber == 0 else 1,
            0 if self.episodeNumber == 0 else 1,
        )

    def normalizeForcomparison(self):
        return (
            re.sub(r"\s+", " ", self.seriesName.strip().lower()),
            self.seasonNumber,
            self.episodeNumber,
            re.sub(r"\s+", " ", self.episodeTitle.strip().lower()),
        )

    def isBetterThan(self, other):
        # We just simply compare the score each episode has
        return self._score() > other._score()

    def isValid(self):
        # If all invalid requirements are met, invalidReasons will be True
        invalidReasons = (
            self.episodeNumber == 0 and self.episodeTitle == "Untitled Episode" and self.airDate == "Unknown"
        )

        # If the show is invalid, we will return False, as the show is NOT valid
        return not invalidReasons