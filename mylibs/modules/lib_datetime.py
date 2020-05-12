from django.contrib import admin
import datetime

date = ''

def getDateObject(y, m, d):
	return datetime.date(y, m, d)

def getYear():
    return date.getNow().year


def getMonth():
    return date.getNow().month


def getDate():
    return date.getNow().date


def getHour():
    return date.getNow().hour


def getAge(birthDate, targetDate=datetime.date.today()):
    age = targetDate.year - birthDate.year
    if birthDate < targetDate:
        age -= 1
    return age

def getSeason():
	month = getMonth()
	if month >= 3 and month <= 5:
		return 'spring'
	elif month >= 6 and month <= 8:
		return 'summer'
	elif month >= 9 and month <= 11:
		return 'autumn'
	else:
		return 'winter'

class Date():
    def __init__(self):
        self.now = datetime.datetime.now()
    

    def getNow(self):
        return self.now

date = Date()