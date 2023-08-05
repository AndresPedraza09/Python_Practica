### Dates ###

from datetime import datetime

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.min)
    print(date.second)
    print(date.timestamp())

print_date(now)

year_2023 = datetime(2023, 1, 1)

print_date(year_2023) 

#Manejar El tiempo 
from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

#Controlar Fechas
from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

#Agregar datos a la fecha ya que por defecto es 0
current_date = date(2022, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

#Operaciones con las fechas 
current_date = date(current_date.year, current_date.month + 1, current_date.day) 
print(current_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)


#print(year_2023.time())


#Sirve para operar con distintas fechas (Trabajar con franjas de fechas)
from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta / start_timedelta)
