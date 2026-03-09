# Technical Challenge Proofpoint - 2026 edition - Proofpoint
## Tasks overview
### Task A: Please, answer the following questions as precise as posible, preferably in English
#### **Status: Solved**
<details>

1. Describe the most relevant learnings from programming-related subjects during your career
2. Describe a situation you had to resolve with a teammate from a study or work group
3. Describe your personal learning plans or development expectations in technical areas in the short and long terms

</details>

### Task B: Practical exercise to solve - The Streaming Service's Lost Episodes
#### **Status: Solved**
<details>
<summary> Context, Goal, Problems & Output </summary>

**Context**

A streaming platform is digitalizing its catalog of series, seasons and episodes. 
However, during the ingestion of data, no validation or uniqueness checks were applied, which resulted in a corrupted catalog containing missing information, inconsistent values, and duplicated episodes.
You will be given a CSV file where each row represents an episode. Each entry should contain the following fields in this order:
- Series Name - name of the series (required)
- Season Number - season number (may be missing or invalid)
- Episode Number - episode number (may be missing or invalid)
- Episode Title (may be missing)
- Air Date - date when the episode aired (may be missing or invalid)
Because of the lack of checks during data entry, the file may contain inconsistencies, incorrect formats, and repeated entries.

**Goal**

Your task is to process this CSV file and produce a clean, corrected and de-duplicated catalog.
You must: 
- Parse and normalize all entries
- Correct missing or invalid information following the rules below
- Detect and remove duplicated episodes
- Keep only one valid record for each unique episode
- Produce a final, well‑organized list of episodes
- Generate a quality report summarizing your corrections
Additional organization (e.g., grouping or sorting) is a plus but not mandatory

**Problems you may encounter in the file**

1. Missing or Empty Fields: The following fields may be empty or missing entirely:

- Series Name: If missing or empty → discard the record (required to identify an episode)
- Season Number: If missing, empty, negative, or not a number → set to 0
- Episode Number: If missing, empty, negative, or not a number → set to 0
- Episode Title: If missing or empty → replace with "Untitled Episode"
- Air Date: If missing, empty, or invalid → replace with "Unknown"
- When Episode Number, Episode Title and Air Date are missing (the three fields), discard the record (required to identify and merge): Consider values 0 and "Unknown" as missing information

2. Invalid Data Formats <br> You may find:

- Non‑numeric values in Season or Episode numbers <br> e.g., "one", "3.5", "--2"
- Impossible dates <br> e.g., "not a date", "2022-40-99", "0000-00-00"
- Extra whitespace, inconsistent capitalization, strange characters, etc. <br> All such cases should be cleaned and normalized.

3. Duplicate Entries <br> Because no uniqueness constraints were enforced during ingestion, the same episode may appear:

- several times,
- with different titles,
- different air dates,
- different spacing or formatting,
- or inconsistent season/episode numbering.

Episodes must be considered duplicates when they refer to the same:

```
(SeriesName_normalized, SeasonNumber, EpisodeNumber)
```
Or
```
(SeriesName_normalized, 0, EpisodeNumber, EpisodeTitle_normalized)
```
Or
```
(SeriesName_normalized, SeasonNumber, 0, EpisodeTitle_normalized)
```

Normalized means: trimmed, collapsed spaces, and lowercased for comparison.

When duplicates exist, you must keep only the “best” record, following this priority:

- Episodes with a valid Air Date over "Unknown"
- Episodes with a known Episode Title over "Untitled Episode"
- Episodes with a valid Season Number and Episode Number
- If still tied → keep the first entry encountered in the file

**Output**

You must provide the source code (any language of your preference) of a program that can read the csv input file. Feel free to
share a Github link if that's easier. The code should generate the following output:
1. Cleaned Episode Catalog
Output file name: episodes_clean.csv
With columns:

```
SeriesName,SeasonNumber,EpisodeNumber,EpisodeTitle,AirDate
```

Requirements:
- All corrections applied
- No duplicates
- Safe defaults used where appropriate
- Each row represents a valid episode

2. Data Quality Report

Output file name: report.md
Must include:
- Total number of input records
- Total number of output records
- Number of discarded entries
- Number of corrected entries
- Number of duplicates detected
- Explanation of the deduplication strategy

This report helps assess data quality and your decision‑making

</details>

### Task C: Word Frequency Analisis
#### **Status: Solved**
<details>

<summary> Description </summary>

Write a program that reads a text file and performs a word frequency analysis:

- The program should be able to read a text file provided as input and count how many times each word appears in the text.

- The word comparison should be case-insensitive and should not consider punctuation or special characters.

- Display the 10 most frequent words, along with their frequency of occurrence.

</details>