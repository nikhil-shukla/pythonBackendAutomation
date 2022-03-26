import csv

filePath = "F://Udemy//pythonProject//BackendAutomation//utilities//loanapp.csv"
with open(filePath, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    # print(list(csvReader))

    names = []
    stats = []
    for row in csvReader:
        # print(row)
        # print(row[0])
        names.append(row[0])
        stats.append(row[1])
print(names)
print(stats)

index = names.index('Joe')
loanStatus = stats[index]
print('loan status is ' + loanStatus)

with open(filePath, 'a') as wFile:
    write = csv.writer(wFile)
    write.writerow(['Bob', 'Rejected'])
