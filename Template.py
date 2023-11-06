from datetime import datetime
# ----------------------------- #
def get_time():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def GEN_Solution():
  # อ่านเฉลยจากกระดาษคำตอบของฝ่ายวิชาการ ซึ่งเป็นไฟล์รูป (PNG, JPG)
  # เก็บเป็นลิสต์ เช่น มี 5 ข้อปรนัย 1 ข้ออัตนัย -> ['1', '3', '5', '2', '4', '0050.00']
  return ลิสต์เฉลย

def Answer_sheet_check():
  # เขียนให้อ่านว่าน้องตอบอะไรมาจากกระดาษคำตอบ
  # เช่น น้องรหัส 68315721 สอบ PreTest
  # format -> [เวลา, '68315721', 'PreTest', '1', '3', '5', '2', '4', '0050.00'] 
  # หากมีปัญหา เช่น ฝนมากกว่า 1 ข้อใส่ทุกข้อที่ตรวจเจอ เช่น '25', '13', ไม่ตอบ ใส่ช่องว่าง ('  ')
  return ลิสต์ที่เก็บข้อมูลจากกระดาษคำตอบ

def Scoreing(A, Sol):
  S = 0
  for i in range(50):  S += (Sol[i] == A[i+x]) * 1.5
  for i in range(10):  S += (Sol[i] == A[i+x]) * 2.5 
  return S
# ----------------------------- #
Solution = GEN_Solution()
Ans = Answer_sheet_check()
Score = Scoreing(Ans, Solution)
print(Score)
