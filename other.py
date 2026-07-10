import random as rd


def statb(): #стать мага
	sex=None
	sexn=rd.randint(0,1)
	if sexn == 1: 
		sex = 'female'
		return sex
	else: 
		sex = 'male'
		return sex


def year():
	yer=rd.randint(1, 4)
	return yer
	
def cursenergy(): #кількість проклятої енергії
	iscursed=rd.randint(1, 30)
	if iscursed<10:
		return 0
	else: 
		curseng=rd.randint(1, 100)
		return curseng


