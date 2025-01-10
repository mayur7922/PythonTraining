import csv

with open('sales.csv', 'r') as file:
    reader = csv.DictReader(file)
    total_sales = 0
    avg_sales = 0.0
    size = 0;
    maxSale = 0
    
    for row in reader:
        size += 1
        sale = int(row['sales'])
        total_sales += sale
        avg_sales += sale
        maxSale = max(maxSale, sale)

    avg_sales /= size

    print("Total sales are : ", total_sales)
    print("Average sales are : ", avg_sales)

    file.seek(0)
    next(reader) 

    for row in reader:
        sale = int(row['sales'])
        if sale == maxSale:
            print("Maximum sold product is : ", row['product'])
            break



    