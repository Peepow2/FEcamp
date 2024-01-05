import fpdf
import os
import time

ss = time.time()
pdf = fpdf.FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(True, margin = 10)
pdf.add_page()

pdf.set_font('helvetica', 'B', 16)
pdf.cell(190, 8, 'FECamp17', border = 0, align = 'C')
pdf.ln()
pdf.cell(190, 15, 'NameSheet of Stupid Academic department', border = 0, align = 'C')
pdf.ln()

HEADER = ["NO", "Student_ID","Name", "Major", "Age", "University"]
TABLE_DATA = [
    ["1", "643XXXXX21", "PP", "Electrical", "21", "Chulalongkorn"],
    ["2", "653XXXXX21", "North 0-3", "Civil", "20", "Old trafford"],
    ["3", "653XXXXX21", "Faro", "Computer", "20", "Chulalongkorn"],
    ["4", "653XXXXX21", "Phum", "Computer", "20", "Chulalongkorn"],
    ["5", "653XXXXX21", "Jai", "Electrical", "20", "Chulalongkorn"],
    ["6", "653XXXXX21", "Confirm", "Electrical", "20", "Chulalongkorn"],
    ["7", "653XXXXX21", "PaoPao", "ICE", "20", "Chulalongkorn"],
    ["8", "653XXXXX21", "Mix", "Civil", "20", "Chulalongkorn"],
]
s = S = len(TABLE_DATA)
while s < int(2e4):
    for j in range(S):
        s += 1
        TABLE_DATA.append([str(s)] + TABLE_DATA[j][1::])

pdf.set_font("Times", size = 12)
headings_style = fpdf.fonts.FontFace(color = (255, 255, 255), fill_color = (0, 102, 255), emphasis="BOLD")

with pdf.table(headings_style = headings_style, \
               col_widths=(0.4, 1, 2, 1, 0.6, 1), \
               text_align=("CENTER")) as table:
    headings = table.row()
    for d in HEADER:
        headings.cell(d)

with pdf.table(first_row_as_headings = False, col_widths=(0.4, 1, 2, 1, 0.6, 1), \
               text_align=("CENTER", "CENTER", "LEFT", "CENTER", "CENTER", "CENTER")) as table:
    for data_row in TABLE_DATA:
        row = table.row()
        for datum in data_row:
            row.cell(datum)

pdf.output("Simple.pdf") # Create ใบรายชื่อ
# ----------------------------------------------- # 
PRINT = False # ปริ้นไฟล์
if PRINT: os.startfile("Simple.pdf", "print")
# ----------------------------------------------- # 
print("Finished")
total = time.time() - ss
print('TIME USED =', int(total // 3600), 'hour', int(total // 60), 'min', int(total % 60) + 1, 'seconds')
