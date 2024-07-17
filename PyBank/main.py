import os
import csv


file_path = 'resources/budget_data.csv'
with open(file_path, mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header
    data = list(reader)

dates = [row[0] for row in data]
profit_losses = [int(row[1]) for row in data]

total_months = len(set(dates))

net_total = sum(profit_losses)

changes = [profit_losses[i] - profit_losses[i - 1] for i in range(1, len(profit_losses))]

average_change = sum(changes) / len(changes)

greatest_increase_amount = max(changes)
greatest_increase_index = changes.index(greatest_increase_amount)
greatest_increase_date = dates[greatest_increase_index + 1]

greatest_decrease_amount = min(changes)
greatest_decrease_index = changes.index(greatest_decrease_amount)
greatest_decrease_date = dates[greatest_decrease_index + 1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

text_path = os.path.join('analysis', 'Export_Financial_Analysis.txt')
with open(text_path,"w") as text_file:
    text_file.write("Financial Analysis" + "\n")
    text_file.write("-----------------------------------------" + "\n")
    text_file.write(f"Total Months: {total_months}" + "\n")
    text_file.write(f"Total: ${(net_total)}" + "\n")
    text_file.write(f"Average Change: ${average_change:.2f}" + "\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})" + "\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})" + "\n")
text_file.close()