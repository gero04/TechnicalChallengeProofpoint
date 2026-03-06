import sys
from catalogProcessor import CatalogProcessor
from reportGenerator import ReportGenerator

def main(inputPath: str, outputDir: str):

    # We define the paths to the output and report
    outputPath = f"{outputDir}/episodes_clean.csv"
    reportPath = f"{outputDir}/report.md"

    # Process the catalog
    processor = CatalogProcessor(inputPath, outputPath, reportPath)
    totalInput, totalOutput, discarded, corrected, duplicates = processor.process()

    # Generate the report
    reporter = ReportGenerator(reportPath)
    reporter.generateReport(totalInput, totalOutput, discarded, corrected, duplicates)

    # Print a summary to the console
    print(f"Input records:  {totalInput}")
    print(f"Output records: {totalOutput}")
    print(f"Discarded:      {discarded}")
    print(f"Corrected:      {corrected}")
    print(f"Duplicates:     {duplicates}")
    print(f"Clean catalog path: {outputPath}")
    print(f"Report path: {reportPath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <input.csv> [output_dir]")
        sys.exit(1)

    input_csv  = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    main(input_csv, output_dir)