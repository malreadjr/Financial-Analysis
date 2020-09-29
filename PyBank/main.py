import os
import csv
from pathlib import Path

def analyze_dates(date_string):
  components = date_string.split("-",1)
  month = components[0]
  year = components[1]

def analyze_profit_loss(profitloss):
    converted_profitloss = float(profitloss)
    print(converted_profitloss)

def print_solution(row_count,totalprofitloss,average_change, monthlyprofitchange,dates):
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months:", row_count)
    print("Total: ","${}".format(sum(totalprofitloss)))
    print("Average  Change:","${}".format(average_change))
    maxint = monthlyprofitchange.index(max(monthlyprofitchange)) + 1
    minint = monthlyprofitchange.index(min(monthlyprofitchange)) + 1
    print("Greatest Increase in Profits:",dates[maxint], "(${})".format(max(monthlyprofitchange)))
    print("Greatest Decrease in Profits:",dates[minint], "(${})".format(min(monthlyprofitchange)))
    
    #File
    output_file = Path(os.path.dirname(__file__),"analysis","outputfile.txt")

    with open(output_file,"w") as file:
        
        file.write("Financial Analysis")
        file.write("\n")
        file.write("----------------------------")
        file.write("\n")
        file.write(f"Total Months:{row_count}")
        file.write("\n")
        file.write(f"Total: ${sum(totalprofitloss)}")
        file.write("\n")
        file.write(f"Average  Change: ${average_change}")
        file.write("\n")
        file.write(f"Greatest Increase in Profits: {dates[maxint]} (${max(monthlyprofitchange)})")
        file.write("\n")
        file.write(f"Greatest Decrease in Profits: {dates[minint]} (${min(monthlyprofitchange)})")

                        
monthlyprofitchange = []
totalprofitloss = []
dates = []


script_path = os.path.dirname(__file__)
file_path = "Resources\\budget_data.csv"
budget_csv = os.path.join(script_path,file_path)

# Open and read csv
with open(budget_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    # Read through each row of data after the header
    previousProfit_Losses = 0
    greatest_decrease = 0
    greatest_increase = 0
    average_change = 0    
    row_count = 0
    for row in csv_reader:   
       analyze_dates(row[0])
       row_count += 1
       totalprofitloss.append(int(row[1]))  
       dates.append(row[0])    
          
    for i in range(len(totalprofitloss)-1):        
        # Take the difference between two months and append to monthly profit change
        monthlyprofitchange.append(totalprofitloss[i+1]-totalprofitloss[i])
    
    indexofmaxmonth = monthlyprofitchange.index(max(monthlyprofitchange)) + 1
    indexofminmonth = monthlyprofitchange.index(min(monthlyprofitchange)) + 1
       
    print_solution(row_count,totalprofitloss,round(sum(monthlyprofitchange)/len(monthlyprofitchange),2),monthlyprofitchange,dates)