import locale
locale.setlocale(locale.LC_ALL, 'th_TH.utf8')
NAME = ['โอนาน่า', 'เดเกอา', 'ฟาน เดอร์ ซาร์', 'ชไมเคิล', 'บายินเดียร์']
Sorted_NAME = sorted(NAME, key = locale.strxfrm)
print(Sorted_NAME)
