
import time
alp_EU =  "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
alp_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
shif = input("(shifr)шифровка/дешифровка(desh) ")
sag = int(input("Шаг шифровки: "))
sags = - + sag
message = input("Сообщение для де/шифровки: ").upper()
itog = " "
lang = input("Выберите язык ru/eu: ")
if shif == "shifr" :
   if lang == "ru":
     for i in message:
        mesto = alp_RU.find(i)
        new_mesto = mesto + sag
        if i in alp_RU:
            itog += alp_RU[new_mesto]
        else:
            itog += i
   else:
     for i in message:
        mesto = alp_EU.find(i)
        new_mesto = mesto + sag
        if i in alp_EU:
            itog += alp_EU[new_mesto]
        else:
            itog += i
else :
  if lang == 'ru':
    for i in message:
        mesto = alp_RU.find(i)
        new_mesto = mesto + sags
        if i in alp_RU:
            itog += alp_RU[new_mesto]
        else:
            itog += i
  else:
    for i in message:
        mesto = alp_EU.find(i)
        new_mesto = mesto + sags
        if i in alp_EU:
            itog += alp_EU[new_mesto]
        else:
            itog += i
reversed=''.join(reversed(itog)) 

print (itog)
print("через 20 секунд программа закроется автоматически")
time.sleep(20)