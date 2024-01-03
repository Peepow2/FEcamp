import json 
# Example DATA
DATA = {
       '6439832412': {"name" : "PP", "age" : 21, "major" : 'Electric', "phonenumber" : "9976770500"},
       '6439218121': {"name" : "LL", "age" : 21, "major" : 'Computer', "phonenumber" : "1815641331"},
        } 
# --------------------------------------------- # แบบที่ 1
# Dict to JSON
fout = open("DATA.json", "w")
json.dump(DATA, fout)
fout.close()

# JSON to Dict
fin = open("DATA.json", "r") 
DATA2 = json.loads(fin.readline())
fin.close()
# --------------------------------------------- # แบบที่ 2
with open("DATA.json", "r") as fout: # Dict to JSON
  json.dump(DATA, fout)
  
with open("DATA.json", "r") as fin:  # JSON to Dict
  json.loads(fin.readline())
