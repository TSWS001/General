import csv
import os

# Open the CSV file
with open('test.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)

    # Iterate over each row in the CSV file
    for row in csv_reader:
        old_name_base = row[0]  # First column: current file base name
        new_name_base = row[1]  # Second column: new file base name
        
        # Check for the correct file extension (.jpeg, .jpg, or .png)
        extensions = ['.jpeg', '.jpg', '.png']
        old_name = None
        
        for ext in extensions:
            if os.path.exists(old_name_base + ext):
                old_name = old_name_base + ext
                break  # Stop checking once we find the correct file
        
        # If the file is found, rename it
        if old_name:
            new_name = new_name_base + ext  # Add the same extension to the new name
            print(f"Renaming: {old_name} -> {new_name}")
            try:
                os.rename(old_name, new_name)
                print(f"Renamed: {old_name} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {old_name}: {e}")
        else:
            print(f"File {old_name_base} not found with any of the extensions {extensions}.")
