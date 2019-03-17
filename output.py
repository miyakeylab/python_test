import csv
with open('test.csv','w') as f:
   writer = csv.writer(f)
   writer.writerow([1,'PHP','Laravel'])
   writer.writerow([2,'Ruby','RubyOnrails'])
   writer.writerow([3,'Python','Django'])