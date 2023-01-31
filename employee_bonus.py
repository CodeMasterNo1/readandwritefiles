import csv

in_file = open("EmployeePay.csv", "r")
csv_reader = csv.reader(in_file)

next(csv_reader)

header = ["ID", "Employee_Name", "Total_Pay"]

print(header)

for row in csv_reader:
    total_pay = int(row[3]) + int(row[3]) * float(row[4])
    print(row[0], row[1] + " " + row[2], round(total_pay, 2))

in_file.close()
