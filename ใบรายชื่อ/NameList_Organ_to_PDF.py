import random
import fpdf

fin = open("score.csv", 'r')
DATA = fin.readlines()
fin.close()

score = list()
for line in DATA:
    line = line.split(',')
    score.append([float(line[1].strip()), line[0]])

score = sorted(score, reverse = True)

'''
SWAP = [[29, 30], ...]
for s in SWAP:
    i, j = s
    score[i], score[j] = score[j], score[i]
'''

fin = open("Name_List.csv", 'r')
DATA = fin.readlines()
fin.close()

D = dict()
for line in DATA:
    line = line.split(',')
    D[line[1]] = line[2:]
# ---------------------------- #
Special_Room = 1
NO_ROOM = 8
Per_Room = 33
ROOM = dict()
RN = "301_Scorcerer 206_Archer 204_Priest 205_Bard 304_Warlock 306_Rogue 404_Druid 409_Barbarian".split()
seq = [int(i) for i in range(Special_Room, 8)]
random.shuffle(seq)

for name in RN:
    ROOM[name] = list()

for i in range(265):
    if i < Special_Room * Per_Room:
        ROOM[RN[i % Special_Room]].append(score[i][1])
    else:
        ROOM[RN[seq[i % (8 - Special_Room)]]].append(score[i][1])
# ---------------------------------------------- #
pdf = fpdf.FPDF('P', 'mm', 'A4')
pdf.set_auto_page_break(True, margin = 15)
pdf.set_top_margin(15)
pdf.set_left_margin(15)
pdf.set_right_margin(15)
pdf.add_font('Th_sarabun_psk', '', 'THSarabun.ttf')
pdf.add_font('Th_sarabun_psk', 'B', 'THSarabun Bold.ttf')

HEADER = ["ลำดับ", "เลขประจำตัว", "ชื่อ - นามสกุล", "ชื่อเล่น", "ลงชื่อ (เช้า)", "ลงชื่อ (ออก)"]
cnt = 0
for key in ROOM:
    seq = 1
    pdf.add_page()
                
    pdf.set_font('Th_sarabun_psk', 'B', 16)
    pdf.cell(180, 8, 'รายชื่อน้องค่าย ห้อง ' + key, border = 0, align = 'C')
    pdf.ln()
    pdf.cell(180, 8, 'โครงการแนะแนวความถนัดทางวิศวกรรมศาสตร์สู่น้องระดับชั้นมัธยมศึกษาตอนปลาย ครั้งที่ 17 (FEcamp 17th)', border = 0, align = 'C')    
    pdf.set_line_width(0.5)
    pdf.line(15, 32, 195, 32)
    
    pdf.set_font('Th_sarabun_psk', '', 16)
    pdf.set_line_width(0.2)
    pdf.ln(12)
    
    size = (8, 17, 30, 15, 15, 15) 
    with pdf.table(width = 180, line_height = 8, col_widths = size, \
                    text_align = ("CENTER")) as table:
        headings = table.row()
        for d in HEADER:
            headings.cell(d)
       
    for ID in sorted(ROOM[key]):
        with pdf.table(width = 180, line_height = 7, first_row_as_headings = False, col_widths = size, \
                       text_align=("CENTER", "CENTER", "LEFT", "CENTER", "C", "C")) as table:
            
            NAME = D[ID][0] + D[ID][1] + ' ' + D[ID][2]
            Nick = D[ID][3].strip()
            ROW = [str(seq), ID, NAME, Nick, '', '']
            row = table.row()
            for datum in ROW:
                row.cell(datum)
            seq += 1
            
pdf.output("Namesheet_After_Pretest.pdf") # Create ใบรายชื่อ
