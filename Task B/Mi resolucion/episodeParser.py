from word2num import word2num
from datetime import datetime
from episode import Episode
import re
class EpisodeParser:
    @staticmethod
    def _parse_int(value: str | int) -> int:
        # In this method we will parse string numbers ("one", "3", "-2") and negative integers
        
        # If we are given an int, but it can be a negative, we return it only if it is positive
        if isinstance(value, int):
            return value if value > 0 else 0
        
        # If we got None, "", "      " trying to pass as a number, here we catch them
        if not value or not value.strip():
            return 0
        
        # Then we try to convert the value to an int
        try:
            # We convert the number to a float, and then to a float ("3.5" can be converted now)
            n = int(float(value.strip()))

            # We return it only if it is positive
            return n if n > 0 else 0
        except ValueError:
            #If we tried to convert the value to an int and it failed (rising ValueError) then we simply return 0
            pass

        # By last we will try to convert the literal number ("one", "twenty three") to an int
        try:
            number = word2num(value)
            return number if number > 0 else 0
        except Exception:
            return 0
    
    @staticmethod
    def _parse_date(valueDate: str) -> str:
        ''' Similar to the int parser, here we parse the date
            We contemplate these cases:
            "" or None -> "Unknown"
            "not a date" -> "Unknown"
            "2022-40-99" -> "Unknown"
            "0000-00-00" -> "Unknown"

            And a "happy" case:
            "2024-06-14" -> "2024-06-14"

            We will assume dates come in YYYY/MM/DD, YYYY-MM-DD, and also DD/MM/YYYY, DD-MM-YYYY formats
        '''
        # First, we discard None, "" or "     " cases
        if not valueDate or not valueDate.strip():
            return "Unknown"
        
        # YYYY-MM-DD cases
        try:
            dt = datetime.strptime(valueDate.strip(), "%Y-%m-%d")
            return "Unknown" if dt.year < 1 else dt.strftime("%Y-%m-%d")
        except ValueError:
            pass

        # YYYY/MM/DD cases
        try:
            dt = datetime.strptime(valueDate.strip(), "%Y/%m/%d")
            return "Unknown" if dt.year < 1 else dt.strftime("%Y-%m-%d")
        except ValueError:
            pass
        # DD-MM-YYYY cases
        try:
            dt = datetime.strptime(valueDate.strip(), "%d-%m-%Y")
            return "Unknown" if dt.year < 1 else dt.strftime("%Y-%m-%d")
        except ValueError:
            pass
        # DD/MM/YYYY cases
        try:
            dt = datetime.strptime(valueDate.strip(), "%d/%m/%Y")
            return "Unknown" if dt.year < 1 else dt.strftime("%Y-%m-%d")
        except ValueError:
            pass

        # If every attempt on parsing fails... then we return Unknown
        return "Unknown"
        
        # All cases return YYYY-MM-DD format
    
    def parse(self, raw:dict) -> Episode | None:
        # Validate Series Name
        if not raw.get("SeriesName", "") or raw.get("SeriesName", "").strip() == "":
            return None, False
        else: 
            seriesName = re.sub(r"\s+", " ", raw.get("SeriesName", "").strip())
        
        # Clean and validate Season Number
        seasonNumber = self._parse_int(raw.get("SeasonNumber", ""))

        # Clean and validate Episode Number
        episodeNumber = self._parse_int(raw.get("EpisodeNumber", ""))

        # Clean and validate Episode Title
        episodeTitle = "Untitled Episode" if (not raw.get("EpisodeTitle", "") or raw.get("EpisodeTitle", "").strip() == "") else raw.get("EpisodeTitle", "")

        # Clean and validate Air Date
        airDate = self._parse_date(raw.get("AirDate", ""))

        # Flag used to check if there where any corrections
        corrections = (
            seriesName != raw.get("SeriesName", "") or
            seasonNumber != raw.get("SeasonNumber", "") or
            episodeNumber != raw.get("EpisodeNumber", "") or
            episodeTitle != raw.get("EpisodeTitle", "") or
            airDate != raw.get("AirDate", "")
        )

        # We validate if Episode Number, Episode Title and Air Date don't exist
        if episodeNumber == 0 and episodeTitle == "Untitled Episode" and airDate == "Unknown":
            return None, False

        # We return the Episode, clean and corrected, and the flag that will be used later in the report
        return Episode(seriesName, seasonNumber, episodeNumber, episodeTitle, airDate), not corrections