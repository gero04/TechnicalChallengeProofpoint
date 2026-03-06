from episode import Episode

class DuplicateDetector:
    def __init__(self):
        self.uniqueEpisodes = []
        self.duplicatesCount = 0
    
    def _isDuplicate(self, episodeA: Episode, episodeB: Episode) -> bool:
        # Here we must implement the 3 rules to see if an episode is duplicate
        
        seriesA, seaNumA, epNumA, epTitA = episodeA.normalizeForcomparison()
        seriesB, seaNumB, epNumB, epTitB = episodeB.normalizeForcomparison()

        # Rule #1: The SERIES NAME, SEASON NUMBER, EPISODE NUMBER are the same
        rule1 = (
            seriesA == seriesB and
            seaNumA == seaNumB and
            epNumA == epNumB
        )

        # Rule #2: The SERIES NAME, EPISODE NUMBER, EPISODE TITLE are the same
        rule2 = (
            seriesA == seriesB and
            epNumA == epNumB and
            epTitA == epTitB
        )
        
        # Rule #3: The SERIES NAME, SEASON NUMBER, EPISODE TITLE are the same
        rule3 = (
            seriesA == seriesB and
            seaNumA == seaNumB and
            epTitA == epTitB
        )

        return rule1 or rule2 or rule3

    def addOrUpdate(self, episode: Episode) -> None:
    # Here we either add an episode (and it is unique) or we update it (it is duplicate)

        # We will start by iterating through the uniqueEpisodes array, getting the episode and it's index
        for i, existingEpisode in enumerate(self.uniqueEpisodes):
            
            # If the current episode is duplicate (episode and existingEpisode are the same episode)
            if (self._isDuplicate(episode, existingEpisode)):

                # We add 1 to our duplicated counter
                self.duplicatesCount += 1

                # Is the new episode (episode) better than the one we already had (existingEpisode)?
                if episode.isBetterThan(existingEpisode):

                    # It is, so we replace it at the i position
                    self.uniqueEpisodes[i] = episode
                
                # It isn't, we remain with existing episode as the best
                return
        
        # The for cicle couldn't find a duplicate for episode, it's new!
        self.uniqueEpisodes.append(episode)

    def getUniqueEpisodes(self) -> list:
        return self.uniqueEpisodes