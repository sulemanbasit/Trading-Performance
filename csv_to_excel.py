import pandas as pd
import os
import openpyxl

def csv_to_json():
    # Prompt user for the CSV file name
    csv_file = input("Enter the CSV file name (with .csv extension): ")

    # Check if the file exists in the current directory
    if not os.path.isfile(csv_file):
        print(f"File '{csv_file}' not found in the current directory.")
        return

    # Read the CSV file
    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading the file: {e}")
        return

    # Check if data exceeds Excel limits
    max_rows, max_cols = 1048576, 16384
    if df.shape[0] > max_rows or df.shape[1] > max_cols:
        print("⚠️ The file is too large for Excel. Converting to JSON instead...")

        # Convert to JSON
        json_file = csv_file.replace('.csv', '.json')
        try:
            df.to_json(json_file, orient='records', lines=True)
            print(f"✅ Successfully converted '{csv_file}' to '{json_file}'.")
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
    else:
        # Convert to Excel if size is within limits
        excel_file = csv_file.replace('.csv', '.xlsx')
        try:
            df.to_excel(excel_file, index=False)
            print(f"✅ Successfully converted '{csv_file}' to '{excel_file}'.")
        except Exception as e:
            print(f"Error exporting to Excel: {e}")

if __name__ == "__main__":
    csv_to_json()