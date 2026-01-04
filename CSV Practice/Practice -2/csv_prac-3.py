import csv

file = "employee.csv"

'''with open(file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        print(r)'''
#10 Rows only
'''with open(file, "r") as f1:
    read = csv.reader(f1)
    c = 0
    for r in read:
        print(r)
        c += 1
        if c == 10:
            break'''
with open(file, "r") as f2:
    read = csv.reader(f2)
    with open("new_list.csv", "w", newline = "") as w:
        writer = csv.writer(w)
        for r in read:#1,3 index
            writer.writerow([r[1],r[3]])
    
