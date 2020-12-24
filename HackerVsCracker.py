#UwU
"""
Infection Security
Coded by Al GQ Infection
Hy UwU Hy
"""

def oi():
	print("*******************************************************")
	print("Infection Security")
	print("Hacking, Securing and Developing")
	print("Coded by Al GQ Infection")
	print("Hacker Vs Cracker")
	print("*******************************************************")
oi()

p1 = {"id": "Hacker",
	"skill": 50}
p2 = {"id": "Cracker",
	"skill": 100}

def latihan(p):
	p["skill"] = p["skill"] + 25

def serangan(y, x):
	if y["skill"] > x["skill"]:
		print("Serangan Mu Berhasil :),", y["id"])

	elif y["skill"] == x["skill"]:
		print("Serangan Mu Seimbang,", y["id"])
		
	else:
		print("Serangan Mu gagal :(,", y["id"])

#Latihanlah Untuk Meningkatkan Skill
latihan(p1)
latihan(p1)

latihan(p1)
serangan(p1, p2)