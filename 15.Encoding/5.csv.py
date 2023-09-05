import csv

# Reading CSV file
print("Reading CSV file:")
with open('15.Encoding\customer.csv', newline='') as csv_file:
    customers = csv.reader(csv_file, delimiter=',')
    for row in customers:
        print(', '.join(row))

print('------------')

# Reading CSV file with header handling
print("Reading CSV file with header handling:")
with open('15.Encoding\customer.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row['id'], row['full_name'], row['age'], row['country'])

# Writing CSV file
print('----------------')
print('Writing CSV file:')
with open('15.Encoding\cities.csv', 'w', newline='') as csv_file:
    fieldnames = ['id', 'name', 'country']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    for i in range(1, 10):
        writer.writerow({'id': i, 'name': "city " + str(i),
                        'country': "country " + str(i)})

print('Done')
