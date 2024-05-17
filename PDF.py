import fpdf
import ID
from Room_organ import *

HEADER1 = ["ลำดับ", "เลขที่นั่งสอบ", "รหัสประจำตัวสอบ", "ชื่อ - นามสกุล", "ลายมือชื่อ"]
HEADER2 = ["ลำดับ", "ชื่อ - นามสกุล", "เวลาออกจากห้อง", "เวลาเข้าห้อง", "ลายมือชื่อ"]

def create_namesheet(FILE_NAME):
    pdf = fpdf.FPDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(True, margin = 15)
    pdf.set_top_margin(15)
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.add_font('Th_sarabun_psk', '', 'THSarabun.ttf')
    pdf.add_font('Th_sarabun_psk', 'B', 'THSarabun Bold.ttf')

    fin = open(FILE_NAME, 'r')
    Dict_Name = dict()

    List_Name = list()
    for line in fin.readlines()[1::]:
        List_Name.append(line.split(','))
        
    size = (15, 25, 30, 60, 40)
    NO_Room = 'x 317 318 319 320 417 418 419 420'.split()
    B = 33
    Page = 0
    
    for R in range(len(List_Name)):
        ln = List_Name[R]
        if R % B == 0 and R != len(List_Name) - 1:
            seq = 1
            Page += 1
            pdf.add_page()
            
            pdf.set_font('Th_sarabun_psk', 'B', 16)
            pdf.cell(180, 8, 'ใบเซ็นชื่อผู้เข้าสอบ', border = 0, align = 'C')
            pdf.ln()
            pdf.cell(180, 8, 'โครงการแนะแนวความถนัดทางวิศวกรรมศาสตร์สู่น้องระดับชั้นมัธยมศึกษาตอนปลาย ครั้งที่ 17 (FEcamp 17th)', border = 0, align = 'C')
            pdf.set_line_width(0.5)
            pdf.line(15, 32, 195, 32)

            pdf.set_font('Th_sarabun_psk', '', 16)
            pdf.ln(11)
            pdf.cell(135, 7, 'Pretest FEcamp 17th', border = 0, align = 'L')
            pdf.ln()
            pdf.cell(120, 7, 'วันที่สอบ: วันเสาร์ที่ 18 พฤษภาคม 2567', border = 0, align = 'L')
            pdf.cell(50, 7, 'เวลาสอบ: 8:30 – 11:30 น', border = 0, align = 'L')
            pdf.ln()
            pdf.cell(120, 7, 'สนามสอบ: อาคารวิศวกรรมศาสตร์ 3 จุฬาลงกรณ์มหาวิทยาลัย', border = 0, align = 'L')
            pdf.cell(50, 7, f'ห้องสอบที่: {Page} ({NO_Room[Page]})', border = 0, align = 'L')
            pdf.ln(9)
            
            pdf.set_line_width(0.2)
            with pdf.table(width = 180, line_height = 7, col_widths = size, \
                            text_align = ("CENTER")) as table:
                headings = table.row()
                for d in HEADER1:
                    headings.cell(d)

        with pdf.table(width = 180, line_height = 6, first_row_as_headings = False, col_widths = size, \
                       text_align=("CENTER", "CENTER", "CENTER", "LEFT", "CENTER")) as table:
            
            Name = ln[1] + ln[2] + '  ' + ln[3]
            ROW = [str(R + 1), str(seq), ID.get_ID(R + 1), Name, '']
            row = table.row()
            for datum in ROW:
                row.cell(datum)
            seq += 1

    pdf.output("Namesheet_Pretest.pdf") # Create ใบรายชื่อ
    return
# ----------------------------------------------- #
def bai_yiao():
    pdf = fpdf.FPDF('P', 'mm', 'A4')
    pdf.set_auto_page_break(True, margin = 15)
    pdf.set_top_margin(15)
    pdf.set_left_margin(15)
    pdf.set_right_margin(15)
    pdf.add_font('Th_sarabun_psk', '', 'THSarabun.ttf')
    pdf.add_font('Th_sarabun_psk', 'B', 'THSarabun Bold.ttf')
        
    size = (15, 55, 30, 30, 40)
    NO_Room = 'x 317 318 319 320 417 418 419 420'.split()
    B = 20
    Page = 0
    
    for i in range(len(NO_Room) - 1):
        Page += 1
        pdf.add_page()
        
        pdf.set_font('Th_sarabun_psk', 'B', 16)
        pdf.cell(180, 8, 'ใบขออนุญาตออกนอกห้องสอบ', border = 0, align = 'C')
        pdf.ln()
        pdf.cell(180, 8, 'โครงการแนะแนวความถนัดทางวิศวกรรมศาสตร์สู่น้องระดับชั้นมัธยมศึกษาตอนปลาย ครั้งที่ 17 (FEcamp 17th)', border = 0, align = 'C')
        pdf.set_line_width(0.5)
        pdf.line(15, 32, 195, 32)

        pdf.set_font('Th_sarabun_psk', '', 16)
        pdf.ln(11)
        pdf.cell(135, 7, 'Pretest FEcamp 17th', border = 0, align = 'L')
        pdf.ln()
        pdf.cell(120, 7, 'วันที่สอบ: วันเสาร์ที่ 18 พฤษภาคม 2567', border = 0, align = 'L')
        pdf.cell(50, 7, 'เวลาสอบ: 8:30 – 11:30 น', border = 0, align = 'L')
        pdf.ln()
        pdf.cell(120, 7, 'สนามสอบ: อาคารวิศวกรรมศาสตร์ 3 จุฬาลงกรณ์มหาวิทยาลัย', border = 0, align = 'L')
        pdf.cell(50, 7, f'ห้องสอบที่: {i+1} ({NO_Room[i+1]})', border = 0, align = 'L')
        pdf.ln(9)
        
        pdf.set_line_width(0.2)
        with pdf.table(width = 180, line_height = 7, col_widths = size, \
                        text_align = ("CENTER")) as table:
            headings = table.row()
            for d in HEADER2:
                headings.cell(d)

        for R in range(20):
            with pdf.table(width = 180, line_height = 7, first_row_as_headings = False, col_widths = size, \
                           text_align=("CENTER", "CENTER", "CENTER", "LEFT", "CENTER")) as table:
                
                row = table.row()
                for i in range(5):
                    if i == 0:
                        row.cell(str((R%20) + 1))
                    else:
                        row.cell(' ')

    pdf.output("Baiyiao_Pretest.pdf") # Create ใบรายชื่อ
# ----------------------------------------------- #

# ----------------------------------------------- #
def namesheet_organization_room(FILE_NAME):
    return
# ----------------------------------------------- #
def namesheet(FILE_NAME):
    create_namesheet(FILE_NAME)
    bai_yiao()
    return 
