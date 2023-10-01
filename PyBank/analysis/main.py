import os
# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


def Average(dict):
    sum_of_averages = 0
    len_of_averages = 0
    for k, v in dict.items():
        sum_of_averages += v
        len_of_averages += 1
    return sum_of_averages/len_of_averages

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    #getting 2nd row
    pre_lne = next(csvreader)
    total_months = 1
    total =  int(pre_lne[1])
    changes = {}

    #starting form 3rd row
    for row in csvreader:
        total_months += 1
        total += int(row[1])
        changes[row[0]] = int(row[1]) - int(pre_lne[1])
        pre_lne = row #storing current row as a previous row
        
    #get the corresponding key for max and min value of the dic
    greatest_inc_month = max(changes, key = lambda x: changes[x] )
    greatest_dec_month = min(changes, key = lambda x: changes[x] )
    greatest_profit_inc = "${:.0f}".format(changes[greatest_inc_month] )
    greatest_profit_dec = "${:.0f}".format(changes[greatest_dec_month] )
    Average_changes = "${:.2f}".format(Average(changes))
    
    
    print('Financial Analysis ')
    print('------------------------- ')
    print('Total Months: ',total_months)
    print('Total:', "${:.0f}".format(total))
    print('Average Change:',Average_changes)
    print('Greatest Increase in Profits:',greatest_inc_month,greatest_profit_inc)
    print('Greatest Decrease in Profits:',greatest_dec_month,greatest_profit_dec)
    
    with open('output.txt', 'w') as op_file:
        op_file.write('Financial Analysis \n \n')
        op_file.write('------------------------- \n \n')
        op_file.write('Total Months: %s \n \n' %(total_months))
        #op_file.write('------------------------- \n \n')
        op_file.write('Total: %s \n \n' %("${:.0f}".format(total)))
        #op_file.write('------------------------- \n \n')
        op_file.write('Average Change: %s \n \n' %(Average_changes))
        #op_file.write('------------------------- \n \n')
        op_file.write("Greatest Increase in Profits: %s (%s)\n \n" % (greatest_inc_month, greatest_profit_inc))
        op_file.write("Greatest Decrease in Profits: %s (%s)\n \n" % (greatest_dec_month, greatest_profit_dec))