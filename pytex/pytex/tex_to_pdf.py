from fpdf import FPDF

class PDF(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, title, ln=1, align='C')

    def chapter_paragraph(self, text):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, text)

def generate_pdf_with_paragraph(text, output_file):
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title("My Document")
    pdf.chapter_paragraph(text)
    pdf.output(output_file)

# Example usage
f = open("pdf_gen.tex", "r")
input_string = f.read()
output_filename = "output.pdf"

generate_pdf_with_paragraph(input_string, output_filename)