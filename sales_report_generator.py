import csv

file = open('sales.csv', 'r')
reader = csv.reader(file)

max_sales = 0
row_count = 0

for row in reader:
	print(f"{row}")
	value = int(row[1])
	row_count +=1
	if value > max_sales:
		max_sales = value

print(f"{max_sales}")

output_file = open('summary.txt', 'w')

output_file.write(f"Total Records Analyzed: {row_count}\n")
output_file.write(f"Maximum Sales Value: {max_sales}\n")

output_file.close()

print("Report successfully generated!")
