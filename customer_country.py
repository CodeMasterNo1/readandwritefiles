import csv

in_file = open("customers.csv", "r")
reader = csv.reader(in_file, delimiter=",")
next(reader)

out_file = open("customer_country.csv", "w")
writer = csv.writer(out_file, delimiter=",")
header = ["Customer Name", "Country"]
writer.writerow(header)
for row in reader:
    writer.writerow([row[1] + " " + row[2], row[4]])

in_file.close()
out_file.close()
