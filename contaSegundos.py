nseg = input("Por favor, entre com o número de segundos que deseja converter: ")

segint = int(nseg)

dias = segint // 86400
segrest1 = segint % 86400
horas = segrest1 // 3600
segrest = segint % 3600
minutos = segrest // 60
segrestfin = segrest % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segrestfin, "segundos.")
