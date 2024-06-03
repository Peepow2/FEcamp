import fpdf
import os
import time

s = time.time()

pdf = fpdf.FPDF('P', 'mm', (182, 257))
pdf.set_auto_page_break(True, margin = 0)
pdf.set_top_margin(0)
pdf.set_left_margin(0)
pdf.set_right_margin(0)

pdf.set_draw_color(0, 0, 0)
pdf.set_fill_color(0, 0, 0)
pdf.add_font('Th_sarabun_psk', 'B', 'THSarabun Bold.ttf')

fin = open('Name_List.csv', 'r')
fin.readline()

cnt = 0
Each = 36

for line in fin:
    cnt += 1
    line = line.split(',')
    ID = line[1]
    NAME = line[2] + line[3] + ' ' + line[4]
    SUBJECT = 'TPAT3 ความถนัดด้านวิทยาศาสตร์ เทคโนโลยี และวิศวกรรมศาสตร์'
    Location = 'ตึก 3 คณะวิศวกรรมศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย'
    Date = '3 มิถุนายน 2567'
    SUB_ID = '71'
    ROOM = '301 302 303 304 305 306 307 308'.split()
    
    pdf.add_page()
    pdf.image('Sheet/TPAT3_B5.png', w = 182, h = 257)
    #pdf.image('Sheet/A-LEVEL_B5.png', w = 182, h = 257)
    pdf.image('FELogoBlackLine.png', x = 15.5, y = 7, w = 34, h = 34)
    
    pdf.set_font('Th_sarabun_psk', 'B', 14)
    pdf.set_xy(x = 75, y = 8)
    pdf.cell(4, 5, NAME, border = 0, align = 'L')
    
    pdf.set_font('Th_sarabun_psk', 'B', 8)
    pdf.set_xy(x = 73, y = 27)
    pdf.cell(4, 5, SUBJECT, border = 0, align = 'L')

    pdf.set_font('Th_sarabun_psk', 'B', 9)
    pdf.set_xy(x = 75, y = 34.5)
    pdf.cell(4, 5, Location, border = 0, align = 'L')
    
    pdf.set_font('Th_sarabun_psk', 'B', 12)
    pdf.set_xy(x = 75, y = 41.5)
    pdf.cell(4, 5, ROOM[cnt//Each], border = 0, align = 'L')
    
    pdf.set_font('Th_sarabun_psk', 'B', 12)
    pdf.set_xy(x = 75, y = 49.5)
    pdf.cell(4, 5, Date, border = 0, align = 'L')
      
    pdf.set_font('Th_sarabun_psk', 'B', 14)
    
    for i in range(len(SUB_ID)):
        pdf.set_xy(x = 128.7 + i*4.45, y = 10.8)
        pdf.cell(4, 5, SUB_ID[i], border = 0, align = 'L')
        pdf.ellipse(x = 129 + i*4.45, y = 16.90 + int(SUB_ID[i])*4.20, w = 3.4, h = 3.4, style = 'DF')
    
    for i in range(len(ID)):
        pdf.set_xy(x = 90.0 + i*4.35, y = 19.5)
        pdf.cell(4, 5, ID[i], border = 0, align = 'L')
        
        pdf.set_xy(x = 140.2 + i*4.45, y = 10.8)
        pdf.cell(4, 5, ID[i], border = 0, align = 'L')
        
        pdf.ellipse(x = 140.6 + i*4.45, y = 16.90 + int(ID[i])*4.20, w = 3.4, h = 3.4, style = 'DF')
    
pdf.output('Simple.pdf')
total = time.time() - s
print('TIME USED =', int(total // 3600), 'hour', int(total // 60), 'min', int(total % 60) + 1, 'seconds')
