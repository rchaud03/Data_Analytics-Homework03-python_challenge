import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

with open(budget_data, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    #output_file = "budget_analysis.txt"
    output_file = os.path.join("analysis", "budget_analysis.txt")

    net_revenue = 0
    months_count = 0
    avg_change = 0
    max_revenue_change = 0
    min_revenue_change = 0
    revenue = []
    revenue_change = []
    date = []
    max_change_month = None
    min_change_month = None

    #Looping through rows of the data
    for row in csv_reader:
        #Calculate how many months by incrementing the month count with each iteration
        months_count = months_count + 1

        net_revenue = net_revenue + int(row[1])  #Total revenue
        revenue.append(row[1])  #Populating a revenue list
        date.append(row[0])  #Populating date list


    #Change in revenue for average and min, max scenarios
    for i in range(len(revenue) - 1):
        change = int(revenue[i + 1]) - int(revenue[i])
        revenue_change.append(change)

    #Average change
    avg_change = abs(sum(revenue_change) / len(revenue_change))

    #Max change
    max_revenue_change = max(revenue_change)
    #Min change
    min_revenue_change = min(revenue_change)
    #Max change period
    max_change_month = str(date[revenue_change.index(max(revenue_change))])
    #Min Change period
    min_change_month = str(date[revenue_change.index(min(revenue_change))])

    #Printing all outputs from above
    print("Final Analysis")
    print("------------------------------------------")
    print(f"Total number of Months: {str(months_count)} \nTotal Revenue: ${str(net_revenue)} \nAverage Change: ${str(round(avg_change,2))} \nGreatest Increase:  {str(max_change_month)}  $ {str(max_revenue_change)} \nGreatest Decrease:  {str(min_change_month)}  ${str(min_revenue_change)}")
# Print to output file
with open(output_file, "w") as txt_file:
    txt_file.write(f"\nFinal Analysis:\n------------------------------------------\nTotal number of Months: {str(months_count)} \nTotal Revenue: ${str(net_revenue)} \nAverage Change: ${str(round(avg_change,2))} \nGreatest Increase:  {str(max_change_month)}  $ {str(max_revenue_change)} \nGreatest Decrease:  {str(min_change_month)}  ${str(min_revenue_change)}\n")
