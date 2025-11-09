# used to run this before loading flat files, for matching row counts.
import os

def count_rows_in_files(folder_path):
    total_count = 0
    results = []

    # going over all the files int he 
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()
                # removing one for header lul
                row_count = len(lines) - 1
                results.append((filename, row_count))
                total_count += row_count

    
    for result in results:
        print(f"{result[0]}: {result[1]} rows")
    print(f"Total: {total_count} rows") 

folder_path = r'path\to\folder'

count_rows_in_files(folder_path)
