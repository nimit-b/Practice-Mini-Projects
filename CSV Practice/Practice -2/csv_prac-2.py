import csv

file = "employee.csv"

print("Read with head")
with open(file, "r") as f: # Read with head
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)
print("Read without head")
with open(file, "r") as f2: # Read with head
    csv_reader2 = csv.reader(f2)
    next(csv_reader2)
    for row in csv_reader2:
        print(row)

# Writing new file With only employee name(index = 1), salary(index = 3)
print("Read with head")
with open(file, "r") as f3:
   csv_reader3 = csv.reader(f3)
   with open("name_sal.csv", "w", newline = "") as w: # Read with head
        csv_writer = csv.writer(w)
        for row in csv_reader3:
            print([row[1], row[3]])
            csv_writer.writerow([row[1], row[3]])



