import csv

# Saving Data

file = "goods.csv"
data = []

#Reading File
with open(file, "r") as sales:
   csv_reader = csv.reader(sales)
   for row in csv_reader:
      data.append(row)
      print(row)
   
# Write new File
with open("new_sales.csv", "w", newline = "") as new_file:
      csv_writer = csv.writer(new_file, delimiter = ",")
      for new_row in data:
          csv_writer.writerow(new_row)
print(data)

# Write new File as Product Name, Category
with open("names.csv", "w", newline = "") as names:
       csv_writer = csv.writer(names, delimiter = ",")
       for new_row in data:
          del new_row[0]
          csv_writer.writerow(new_row)
print(data)
