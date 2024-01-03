import json 
# Example DATA
DATA = {
       '6439832412': {"name" : "PP", "age" : 21, "major" : 'Electric', "phonenumber" : "9976770500"},
       '6439218121': {"name" : "LL", "age" : 21, "major" : 'Computer', "phonenumber" : "1815641331"},
        } 
# --------------------------------------------- # แบบที่ 1
fout = open("DATA.json", "w") # Dict to JSON
json.dump(DATA, fout)
fout.close()


fin = open("DATA.json", "r") # JSON to Dict
DATA2 = json.loads(fin.readline())
fin.close()
# --------------------------------------------- # แบบที่ 2
with open("DATA.json", "r") as fout: # Dict to JSON
  json.dump(DATA, fout)
  
with open("DATA.json", "r") as fin:  # JSON to Dict
  json.loads(fin.readline())
