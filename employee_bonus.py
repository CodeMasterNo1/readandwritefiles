import csv

in_file = open("EmployeePay.csv", "r")
csv_reader = csv.reader(in_file)

next(csv_reader)

header = ["ID", "Employee_Name", "Total_Pay"]

print(header)

for row in csv_reader:
    print(row[0], row[1] + " " + row[2], int(row[3]) + int(row[3]) * float(row[4]))

in_file.close()
