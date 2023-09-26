from bill import Bill
from flatmate import Flatmate
from pdfreport import PdfReport

bill = Bill(5000, "september")
flatmate1 = Flatmate(name="john", days=10, month=bill.month)
flatmate2 = Flatmate(name="earnstein", days=14, month=bill.month)
bill1, bill2 = flatmate1.calculate_bill(bill.amount, flatmate1.days, flatmate2.days)
pdf_report = PdfReport(bill.month, flatmate1.name, flatmate2.name, bill1, bill2, bill.amount)
pdf_report.generate("2023")