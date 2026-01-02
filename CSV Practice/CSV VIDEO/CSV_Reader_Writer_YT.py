import csv

file = "employee_data.csv"


#Reading
with open(file, "r") as read:
    csv_reader = csv.reader(read)
    #Write
    with open("name_salary1.csv", "w", newline = "") as new_file:
        csv_writer = csv.writer(new_file)
        for row in csv_reader:
            csv_writer.writerow(row[1:4])  #1 -> 3, 4->Stop


        
    
