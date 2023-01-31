import csv

in_file = open("sales.csv", "r")
csv_reader = csv.reader(in_file)
headers = next(csv_reader)

out_file = open("salesreport.csv", "w", newline="")
writer = csv.writer(out_file)
writer.writerow(["CustomerID", "GrandTotal"])

old_customer_id = None
grand_total = 0

for row in csv_reader:
    customer_id = row[0]
    if old_customer_id != customer_id:
        if old_customer_id is not None:
            writer.writerow([old_customer_id, round(grand_total, 2)])
        old_customer_id = customer_id
        grand_total = 0
    grand_total += float(row[3]) + float(row[4]) + float(row[5])

writer.writerow([old_customer_id, grand_total])

in_file.close()
out_file.close()
