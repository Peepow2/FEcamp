import locale
locale.setlocale(locale.LC_ALL, 'th_TH.utf8')
NAME = ['โอนาน่า', 'เดเกอา', 'ฟาน เดอร์ ซาร์', 'ชไมเคิล', 'บายินเดียร์']

# ------------------------------------------------------------------------ #
Sorted_NAME = sorted(NAME, key = locale.strxfrm) # เรียงตามพจนานุกรม
print(Sorted_NAME)

Sorted_NAME = sorted(NAME) # เรียงตาม...
print(Sorted_NAME)
# ------------------------------------------------------------------------ #
