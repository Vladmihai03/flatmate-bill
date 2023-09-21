from flat import Bill, Flatmate
from report import PdfReport

bill = Bill(float(input('Hey user, enter the bill amount: ')), input('Now, I want the month and the year: '))

ft1 = Flatmate(input('The name of the first flatmate: '), int(input('And now his/her age: ')))
ft2 = Flatmate(input('The name of the second flatmate: '), int(input('Again his/her age: ')))

pdf_report = PdfReport(filename=f'files/{bill.period}.pdf')
pdf_report.generate(flatmate1=ft1, flatmate2=ft2, bill=bill)
