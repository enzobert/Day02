date = input("Donne ton année pour savoir si elle est bissextile:\n")
date = int(date)

if(date%4==0 and date%100!=0 or date%400==0):
  print("positif")
else:
  print("négatif")
