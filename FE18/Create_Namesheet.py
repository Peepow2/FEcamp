def config():
    # ใส่ลิสต์ของเลขห้อง เช่น 'x 317 318 319'.split() หรือ ['x', '317', '318', ...]
    No_ROOM = 'x 317 318 319 320 321 322 323 324 325'.split();

    # ใส่ชื่องาน เช่น 'Pretest FEcamp 17th'
    Event = "FEST BY FE18"

    # วันที่สอบ เช่น 'วันที่สอบ: วันเสาร์ที่ 18 พฤษภาคม 2567'
    DAY = 'วันที่สอบ: XXX'
    
    # เวลาสอบ เช่น 'เวลาสอบ: 8:30 – 11:30 น'
    TIME = 'เวลาสอบ: XXX'

    # สถานที่สอบ เช่น 'สนามสอบ: อาคารวิศวกรรมศาสตร์ 3 จุฬาลงกรณ์มหาวิทยาลัย'
    Exam_Hall = 'สนามสอบ: XXX'

    # ชื่อโครง -> 'โครงการแนะแนวความถนัดทางวิศวกรรมศาสตร์สู่น้องระดับชั้นมัธยมศึกษาตอนปลาย ครั้งที่ 17 (FEcamp 17th)
    KLONG = "จำลองสอบเสมือนจริง"

    return [No_ROOM, KLONG, Event, DAY, TIME, Exam_Hall]

# ---- End Config ----------------------------------

def get_ID(I):
    ID = '682' + ('0000' + str(I))[-4:] 
    
    CheckSum = "9354287"
    S = 0
    for i in range(len(ID)):
        S += int(ID[i]) * int(CheckSum[i]) + int(CheckSum[i])

    ID += str(S % 10)
    return ID

# ---- End get_ID ----------------------------------


import fpdf

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
    B, Page = 36, 0
    No_ROOM, KLONG, Event, DAY, TIME, Exam_Hall = config()
    
    for R in range(len(List_Name)):
        ln = List_Name[R]
        if R % B == 0 and R != len(List_Name) - 1:
            seq = 1
            Page += 1
            pdf.add_page()
            
            pdf.set_font('Th_sarabun_psk', 'B', 16)
            pdf.cell(180, 8, 'ใบเซ็นชื่อผู้เข้าสอบ', border = 0, align = 'C')
            pdf.ln()
            pdf.cell(180, 8, KLONG, border = 0, align = 'C')
            pdf.set_line_width(0.5)
            pdf.line(15, 32, 195, 32)

            pdf.set_font('Th_sarabun_psk', '', 16)
            pdf.ln(11)
            pdf.cell(135, 7, Event, border = 0, align = 'L')
            pdf.ln()
            pdf.cell(120, 7, DAY, border = 0, align = 'L')
            pdf.cell(50, 7, TIME, border = 0, align = 'L')
            pdf.ln()
            pdf.cell(120, 7, Exam_Hall, border = 0, align = 'L')
            pdf.cell(50, 7, f'ห้องสอบที่: {Page} ({No_ROOM[Page]})', border = 0, align = 'L')
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
            ROW = [str(R + 1), str(seq), get_ID(ln[0]), Name, '']
            row = table.row()
            for datum in ROW:
                row.cell(datum)
            seq += 1

    pdf.output("Namesheet.pdf") # Create ใบรายชื่อ
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
    B, Page = 36, 0
    No_ROOM, KLONG, Event, DAY, TIME, Exam_Hall = config()
    
    for i in range(len(No_ROOM) - 1):
        Page += 1
        pdf.add_page()
        
        pdf.set_font('Th_sarabun_psk', 'B', 16)
        pdf.cell(180, 8, 'ใบขออนุญาตออกนอกห้องสอบ', border = 0, align = 'C')
        pdf.ln()
        pdf.cell(180, 8, KLONG, border = 0, align = 'C')
        pdf.set_line_width(0.5)
        pdf.line(15, 32, 195, 32)

        pdf.set_font('Th_sarabun_psk', '', 16)
        pdf.ln(11)
        pdf.cell(135, 7, Event, border = 0, align = 'L')
        pdf.ln()
        pdf.cell(120, 7, DAY, border = 0, align = 'L')
        pdf.cell(50, 7, TIME, border = 0, align = 'L')
        pdf.ln()
        pdf.cell(120, 7, Exam_Hall, border = 0, align = 'L')
        pdf.cell(50, 7, f'ห้องสอบที่: {i+1} ({No_ROOM[i+1]})', border = 0, align = 'L')
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

    pdf.output("Baiyiao.pdf") # Create ใบรายชื่อ
# ----------------------------------------------- #

# ----------------------------------------------- #
def namesheet(FILE_NAME):
    create_namesheet(FILE_NAME)
    bai_yiao()
    return 
# ------------------------------------------------- #

namesheet("Name_list.csv")
