from fpdf import FPDF

name = input("Name: ")

pdf = FPDF("P", "mm", "A4")
pdf.set_auto_page_break(False)
pdf.add_page()

pdf.set_font("Helvetica", "B", 24)
pdf.cell(0, 20, "CS50 Shirtificate", align="C")

pdf.image("shirtificate.png", x=10, y=60, w=190)

pdf.set_font("Helvetica", "B", 20)
pdf.set_text_color(255, 255, 255)
pdf.set_xy(0, 140)
pdf.cell(210, 10, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
