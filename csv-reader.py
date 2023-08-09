import csv
from app import agent

def read_csv_file(file_path):
    try:
        with open(file_path, newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            
            # Skip the header row
            header = next(csvreader)
            
            for row in csvreader:
                print(', '.join(row))
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.csv' with the path to your CSV file
file_path = 'leads.csv'
read_csv_file(file_path)
