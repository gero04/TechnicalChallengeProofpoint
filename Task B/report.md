
# Data Quality Report
## Technical Challenge Intern Program - Proofpoint - March 2026
### Records statistics
- **Total input records:** 41
- **Total output records:** 25
- **Discarded records:** 4
- **Corrected records:** 0
- **Duplicated records:** 12
### Used de-duplication strategy explanation
I've separated the duplication logic in its own class, as OOP  paradigm suggests, and the class has two distinct attributes:
- uniqueEpisodes: An array were we will be saving the episodes, after analizing if they are unique or not. If they aren't unique, we will apply some strategies in order to determine which of the copies to save
- duplicatesCount: An int variable that will be used for the report
The class also has three methods:
- getUniqueEpisodes(): Getter for the uniqueEpisodes attribute
- _isDuplicate(): The method receives episode A and episode B as parameters. After normalizing each episode for comparison, it extracts the variables seriesName, seasonNumber, episodeNumber, and episodeTitle, storing them in the variables seriesA, seasonNumberA, episodeNumberA, and episodeTitleA. Then, using the three rules mentioned in the instructions, it creates variables that will store a Boolean value (rule1, rule2, rule3). If any of the rules are met, the value of the corresponding variable will be true. Finally, it returns true if any rule was met, or false if none of the three rules were met.
- addOrUpdate(): The method processes a given episode to maintain a collection of unique episodes. It begins by iterating through the current list of unique episodes, checking each existing episode against the new one using the `_isDuplicate` method to determine if they represent the same logical episode according to the defined rules. If a duplicate is found, the duplicate counter is incremented, and then the method compares the two episodes using `isBetterThan`. If the new episode is better than the existing one, it replaces the existing episode at that position; otherwise, the existing episode is retained and the method returns without adding the new episode. If no duplicate is found after examining all entries, the new episode is appended to the list as a unique record. 

This de-duplication approach ensures that the final list contains only the best and unique representation for each distinct episode.
