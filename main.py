from flat import Bill, Flatmate
from report import PdfReport, Filesharer


bill_amount = float(input("How much was the bill? "))
bill_period = input("What month and year is the bill? ")

flatmate1_name = input("What is your name? ")
days_in_house1 = int(input("How many days did you stay in the house? "))

flatmate2_name = input("What is your flatmate's name? ")
days_in_house2 = int(input("How many days did they stay in the house? "))

the_bill = Bill(amount=bill_amount, period=bill_period)
flatmate1 = Flatmate(name=flatmate1_name, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=flatmate2_name, days_in_house=days_in_house2)

print(f"{flatmate1_name} pays:  {flatmate1.pays(bill=the_bill, flatmate2=flatmate2)}")
print(f"{flatmate2_name} pays: {flatmate2.pays(bill=the_bill, flatmate2=flatmate1)}")

report = PdfReport(filename=f"{the_bill.period}.pdf")
report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=the_bill)

file_sharer = Filesharer(filepath=report.filename)
print(file_sharer.share())
