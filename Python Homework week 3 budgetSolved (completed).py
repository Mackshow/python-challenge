#import libs
import csv
import os

     #set variables
count = 0 
total = 0 

    #set blink list
profits = []
profit2  = []

    #access file on system
fh = os.path.join("bdata.csv")

    #used csv reader to read csv file ## Split lines using delimiter
with open(fh) as csv_file:
    reader = csv.reader(csv_file, delimiter = ",")

    #Retrieve header
    csv_header = next(reader)
    print(f'Header: {csv_header}')

    # counter to count each row   
    for row in reader:
        count = count + 1 
        if float(row[1]) <= 1000000000000000 :        #any float in row 1 less than Contiton 
            profits.append((str(row[0]), float(row[1])))   #append profit[str,float] specifically

changes = [profits[i+1][1] - profits[i][1] for i in range(len(profits)-1)]

avChange = sum(changes) / len(changes)
 
pt_string = sum([profit[1] for profit in profits])
great_month = ""
great_inc = 0
average = pt_string / count  
with open('budgettxt.txt', 'a') as f: 
    print(f"\nFinancial Analysis\n\n-------------------------\n\nTotal Months: {count}\n\nTotal: ${pt_string}", file=f)
    print(f"\nAverage Change: ${avChange}", file=f)

for i in range(1, len(profits)):    # This iterates through profits Row 1
    diff = abs(profits[i][1] - profits[i-1][1])   #cal absolute value between 2 sequential rows 
    if diff > great_inc:                        #
        great_inc = diff                          #and store in diff if greater than great_inc = 0 
        great_month = profits[i][0]                #also stores month of corrosponding values 
    
with open('budgettxt.txt', 'a') as f:    
    print(f"\nGreatest Increase in Profits: {great_month} $({great_inc})", file=f)       #prints Month and greatest increse as abs value


#had to great new for loop becasue abs() screws up cal for greats decrease. 
gtdc = 0
m2 = ""
for i in range(1, len(profits)):    # This iterates through profits Row 1
    diff = profits[i][1] - profits[i-1][1]  #sub tract starting row from next row 
    if diff < gtdc:                        #
        gtdc = diff                          #and store in diff if less than gtdc = 0 
        m2 = profits[i][0]                #also stores month of corrosponding values 
with open('budgettxt.txt', 'a') as f:    
    print(f"\nGreatest Decrease in Profits: {m2} $({gtdc})", file=f)       #prints Month and greatest decrease 

