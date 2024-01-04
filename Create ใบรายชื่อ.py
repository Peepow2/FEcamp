import fpdf
import os

# Create PDF Object
# Layout ('P', 'L') P = แนวตั้ง L แนวนอน
# Unit ('mm', 'cm', 'in') หน่วยความยาว
# ขนาดกระดาษ ('A3', 'A4', 'Letter', (w, h)) # กำหนดเองได้

# แนวตั้งขนาด A4 หน่วยวัด mm
pdf = fpdf.FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(True, margin = 10)
# Add a page
pdf.add_page()

# fonts ('th sarabun psk', 'angsana new')
# B ตัวหนา ,U เส้นใต้ ,I ตัวเอียง, '' ปกติ, ('BU') ตัวหนาและขีดเส้นใต้
pdf.set_font('helvetica', 'B', 16)
pdf.cell(190, 8, 'FECamp17', border = 0, align = 'C')
pdf.ln() # ขึ้นบรรทัดใหม่
pdf.cell(190, 8, 'NameSheet of Stupid Academic department', border = 0, align = 'C')
pdf.ln()

TABLE_DATA = [
    ["NO", "Student_ID","Name", "Major", "Age", "University"],
    ["1", "643XXXXX21", "PP", "Electrical", "21", "Chulalongkorn"],
    ["2", "653XXXXX21", "North 0-3", "Civil", "20", "Old trafford"],
    ["3", "653XXXXX21", "Faro", "Computer", "20", "Chulalongkorn"],
    ["4", "653XXXXX21", "Phum", "Computer", "20", "Chulalongkorn"],
    ["5", "653XXXXX21", "Jai", "Electrical", "20", "Chulalongkorn"],
    ["6", "653XXXXX21", "Comfirm", "Electrical", "20", "Chulalongkorn"],
    ["7", "653XXXXX21", "PaoPao", "ICE", "20", "Chulalongkorn"],
    ["8", "653XXXXX21", "Mix", "Civil", "20", "Chulalongkorn"],
]
s = len(TABLE_DATA) - 1
S = len(TABLE_DATA)
for i in range(1, 1250): # เปรียบเหมือนมีเด็ก 1250 * 8 = 10000 คน
    for j in range(1, S):
        s += 1
        TABLE_DATA.append([str(s)] + TABLE_DATA[j][1::])

pdf.set_font("Times", size = 9)
headings_style = fpdf.fonts.FontFace(color = (255, 255, 255), fill_color = (0, 102, 255))
with pdf.table(headings_style=headings_style, \
               text_align=("CENTER", "CENTER", "LEFT", "CENTER", "CENTER", "CENTER"), \
               col_widths=(0.4, 1, 2, 1, 0.6, 1)) as table:
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
