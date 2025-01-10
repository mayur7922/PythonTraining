import csv

# reading

with open('csvFile.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# reading with DictReader

with open('csvFile.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

# writing

# newline='', this argument is used to avoid extra blank spaces between rows

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['Name', 'Age', 'City'])
    
    writer.writerow(['Alice', '25', 'New York'])
    writer.writerow(['Bob', '30', 'Boston'])
    writer.writerow(['Charlie', '28', 'Chicago'])

# writing using DictWriter

data = [
    {'Name': 'Alice', 'Age': 25, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 30, 'City': 'Boston'},
    {'Name': 'Charlie', 'Age': 28, 'City': 'Chicago'}
]

with open('file.csv', 'w', newline='') as file:
    fieldnames = ['Name', 'Age', 'City']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    # Write header
    writer.writeheader()
    
    # Write rows
    writer.writerows(data)

# Appending

with open('file.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['David', '35', 'San Francisco'])

