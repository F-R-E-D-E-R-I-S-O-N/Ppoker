# Это покер на пайтоне
import random

randmast = random.randint(1, 4)
randzn = random.randint(2, 14)

randmast1 = random.randint(1, 4)
randzn1 = random.randint(2, 14)

randmast2 = random.randint(1, 4)
randzn2 = random.randint(2, 14)

randmast3 = random.randint(1, 4)
randzn3 = random.randint(2, 14)

randmast4 = random.randint(1, 4)
randzn4 = random.randint(2, 14)

randmast5 = random.randint(1, 4)
randzn5 = random.randint(2, 14)

randmast6 = random.randint(1, 4)
randzn6 = random.randint(2, 14)



while randmast5 == randmast and randzn5 == randzn or randmast5 == randmast1 and randzn5 == randzn1 or randmast5 == randmast2 and randzn5 == randzn2 or randmast5 == randmast3 and randzn5 == randzn3 or randmast5 == randmast4 and randzn5 == randzn4 or randmast5 == randmast6 and randzn5 == randzn6:
    randmast5  = random.randint(1, 4)
    randzn5  = random.randint(2, 14)
while randmast4 == randmast and randzn4 == randzn or randmast4 == randmast1 and randzn4 == randzn1 or randmast4 == randmast2 and randzn4 == randzn2 or randmast4 == randmast3 and randzn4 == randzn3 or randmast4 == randmast5 and randzn4 == randzn5 or randmast4 == randmast6 and randzn4 == randzn6:
    randmast4  = random.randint(1, 4)
    randzn4  = random.randint(2, 14)
while randmast3 == randmast and randzn3 == randzn or randmast3 == randmast1 and randzn3 == randzn1 or randmast3 == randmast2 and randzn3 == randzn2 or randmast3 == randmast4 and randzn3 == randzn4 or randmast3 == randmast5 and randzn3 == randzn5 or randmast3 == randmast6 and randzn3 == randzn6:
    randmast3  = random.randint(1, 4)
    randzn3 = random.randint(2, 14)
while randmast2 == randmast and randzn2 == randzn or randmast2 == randmast1 and randzn2 == randzn1 or randzn2 == randzn3 and randmast2 == randmast3 or randmast2 == randmast4 and randzn2 == randzn4 or randmast2 == randmast5 and randzn2 == randzn5 or randmast2 == randmast6 and randzn3 == randzn6:
    randmast2  = random.randint(1, 4)
    randzn2  = random.randint(2, 14)
while randmast1 == randmast and randzn1 == randzn or randmast1 == randmast2 and randzn1 == randzn2 or randzn1 == randzn3 and randmast1 == randmast3 or randmast1 == randmast4 and randzn1 == randzn4 or randmast1 == randmast5 and randzn1 == randzn5 or randmast1 == randmast6 and randzn1 == randzn6:
    randmast1  = random.randint(1, 4)
    randzn1  = random.randint(2, 14)
while randmast6 == randmast and randzn6 == randzn or randmast6 == randmast1 and randzn6 == randzn1 or randzn6 == randzn3 and randmast6 == randmast3 or randmast6 == randmast4 and randzn6 == randzn4 or randmast6 == randmast5 and randzn6 == randzn5 or randmast6 == randmast2 and randzn6 == randzn2:
    randmast6  = random.randint(1, 4)
    randzn6  = random.randint(2, 14)

card = str(randmast) + str(randzn)
card1 = str(randmast1) + str(randzn1)
card2 = str(randmast2) + str(randzn2)
card3 = str(randmast3) + str(randzn3)
card4 = str(randmast4) + str(randzn4)
card5 = str(randmast5) + str(randzn5)
card6 = str(randmast6) + str(randzn6)

if int(randzn) > 10:
    if randzn == 11:
        randzn = 'Валет'
    if randzn  == 12:
        randzn = 'Дама'
    if randzn == 13:
        randzn = 'Кароль'
    if randzn == 14:
        randzn = 'Туз'
if randmast == 1:
    randmast = str('❤')
if randmast == 2:
    randmast ='◆'
if randmast == 3:
    randmast = '✙'
if randmast == 4:
    randmast = '♠'






if int(randzn1) > 10:
    if randzn1 == 11:
        randzn1 = 'Валет'
    if randzn1  == 12:
        randzn1 = 'Дама'
    if randzn1 == 13:
        randzn1 = 'Кароль'
    if randzn1 == 14:
        randzn1 = 'Туз'
if randmast1 == 1:
    randmast1 = str('❤')
if randmast1 == 2:
    randmast1 ='◆'
if randmast1 == 3:
    randmast1 = '✙'
if randmast1 == 4:
    randmast1 = '♠'





  # МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ МОИ КАРТЫ





if int(randzn2) > 10:
    if randzn2 == 11:
        randzn2 = 'Валет'
    if randzn2 == 12:
        randzn2 = 'Дама'
    if randzn2 == 13:
        randzn2 = 'Кароль'
    if randzn2 == 14:
        randzn2 = 'Туз'
if randmast2 > 0:
    if randmast2 == 1:
        randmast2 = str('❤')
    if randmast2 == 2:
        randmast2 ='◆'
    if randmast2 == 3:
        randmast2 = '✙'
    if randmast2 == 4:
        randmast2 = '♠'







if int(randzn3) > 10:
    if randzn3 == 11:
        randzn3 = 'Валет'
    if randzn3 == 12:
        randzn3 = 'Дама'
    if randzn3 == 13:
        randzn3 = 'Кароль'
    if randzn3 == 14:
        randzn3 = 'Туз'
if randmast3 > 0:
    if randmast3 == 1:
        randmast3 = str('❤')
    if randmast3 == 2:
        randmast3 ='◆'
    if randmast3 == 3:
        randmast3 = '✙'
    if randmast3 == 4:
        randmast3 = '♠'







if int(randzn4) > 10:
    if randzn4 == 11:
        randzn4 = 'Валет'
    if randzn4 == 12:
        randzn4 = 'Дама'
    if randzn4 == 13:
        randzn4 = 'Кароль'
    if randzn4 == 14:
        randzn4 = 'Туз'
if randmast4 > 0:
    if randmast4 == 1:
        randmast4 = str('❤')
    if randmast4 == 2:
        randmast4 ='◆'
    if randmast4 == 3:
        randmast4 = '✙'
    if randmast4 == 4:
        randmast4 = '♠'







if int(randzn5) > 10:
    if randzn5 == 11:
        randzn5 = 'Валет'
    if randzn5 == 12:
        randzn5 = 'Дама'
    if randzn5 == 13:
        randzn5 = 'Кароль'
    if randzn5 == 14:
        randzn5 = 'Туз'
if randmast5 > 0:
    if randmast5 == 1:
        randmast5 = str('❤')
    if randmast5 == 2:
        randmast5 ='◆'
    if randmast5 == 3:
        randmast5 = '✙'
    if randmast5 == 4:
        randmast5 = '♠'







if int(randzn6) > 10:
    if randzn6 == 11:
        randzn6 = 'Валет'
    if randzn6 == 12:
        randzn6 = 'Дама'
    if randzn6 == 13:
        randzn6 = 'Кароль'
    if randzn6 == 14:
        randzn6 = 'Туз'
if randmast6 > 0:
    if randmast6 == 1:
        randmast6 = str('❤')
    if randmast6 == 2:
        randmast6 ='◆'
    if randmast6 == 3:
        randmast6 = '✙'
    if randmast6 == 4:
        randmast6 = '♠'

# Моментик конкатенации карт






print('Твои карты:\n1)   ', randzn, randmast, "\n2)   ", randzn1, randmast1)
print('-----------------------------------------------------------------------------')
print(' На столе лежат:')
print('       |', randzn2, randmast2, " | ", randzn3, randmast3, " | ", randzn4, randmast4, " | ", randzn5, randmast5, " | ", randzn6, randmast6, " | ")
print('-----------------------------------------------------------------------------')


    #  card = str(randzn) + str(randmast)
    #  card1 = str(randzn1) + str(randmast1)
    #  card2 = str(randzn2) + str(randmast2)
    #  card3 = str(randzn3) + str(randmast3)
    #  card4 = str(randzn4) + str(randmast4)
    #  card5 = str(randzn5) + str(randmast5)
    #  card6 = str(randzn6) + str(randmast6)




















if randzn == randzn1 and randmast != randmast1 or randzn == randzn2 and randmast != randmast2 or randzn == randzn3 and randmast != randmast3 or randzn == randzn4 and randmast != randmast4 or randzn == randzn5 and randmast != randmast5 or randzn == randzn6 and randmast != randmast6:
    print('пара из', randzn)
if randzn1 == randzn2  and randmast1 != randmast2 or randzn1 == randzn3  and randmast1 != randmast3 or randzn1 == randzn4   and randmast1 != randmast4 or randzn1 == randzn5  and randmast1 != randmast5 or randzn1 == randzn6  and randmast1 != randmast6:
    print('пара из', randzn1)
if randzn2 == randzn3  and randmast2 != randmast3 or randzn2 == randzn4 and randmast2 != randmast4 or randzn2 == randzn5 and randmast2 != randmast5 or randzn2 == randzn6 and randmast2 != randmast6:
    print('пара из', randzn2)
if randzn3 == randzn4 and randmast3 != randmast4 or randzn3 == randzn5 and randmast3 != randmast5 or randzn3 == randzn6 and randmast3 != randmast6:
    print('пара из', randzn3)
if randzn4 == randzn5 and randmast4 != randmast5 or randzn4 == randzn6 and randmast4 != randmast6:
    print('пара из', randzn4)
if randzn5 == randzn6 and randmast5 != randmast6:
    print('пара из', randzn5)
else:
    print('Нет пар')