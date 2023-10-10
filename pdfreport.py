import webbrowser

from fpdf import FPDF as PDF


class PdfReport:
    """
    Creates a pdf report
    """

    def __init__(self, month, flatmate1, flatmate2, bill1, bill2, bill):
        self.month = month
        self.flatmate1 = flatmate1
        self.flatmate2 = flatmate2
        self.bill1 = bill1
        self.bill2 = bill2
        self.bill = bill

    def generate(self, year):
        pdf = PDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()
        pdf.image("files/house.png", w=10)

        # Report Title
        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=160, h=20, txt="Flatmates Bill", align="C", ln=1)

        # Bill Table Header

        pdf.set_font(family="Times", size=12, style="B")
        pdf.cell(w=30, h=8, txt="Period")
        pdf.cell(w=70, h=8, txt=f"{self.month.title()} {year}", ln=1)

        # Bill Data

        for i in range(1):
            pdf.set_font(family="Times", size=10)
            pdf.set_text_color(80, 80, 80)
            pdf.cell(w=30, h=8, txt=f"{self.flatmate1.title()}")
            pdf.cell(w=70, h=8, txt=f"{self.bill1}", ln=1)
            pdf.cell(w=30, h=8, txt=f"{self.flatmate2.title()}")
            pdf.cell(w=70, h=8, txt=f"{self.bill2}", ln=1)

        pdf.set_font(family="Times", size=12, style="B")
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=30, h=20, txt=f"Total bill is {self.bill}", ln=1)
        # Report output
        pdf.output(f"report for {self.month} {year}.pdf")
        webbrowser.open(f"report for {self.month} {year}.pdf")