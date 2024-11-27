# #Oefening 1
# naam = "Sattawat"
# stad = "Wevelgem"
# bericht = naam + " " + stad
# print(bericht)

# #Oefening 2
# leeftijd = 34
# huidig_jaar = 2024
# geboortejaar = huidig_jaar - leeftijd
# print(geboortejaar)

# #Oefening 3
# getal1 = 8
# getal2 = 4
# som = getal1 + getal2
# verschil = getal1 - getal2
# product = getal1 * getal2
# quotatie = getal1 / getal2
# print(som)
# print(verschil)
# print(product)
# print(quotatie)

# kleur = "blauw"
# kleur += " " "en geel"
# print(kleur)

#is_weer_goed = True
#heeft_je_werk = False
#print("is het weer goed?", is_weer_goed)
#print("heb je werk?", heeft_je_werk)

# leeftijd = 16
# if leeftijd >= 18:
#     print("Je mag gaan stemmen")
# else:
#     print("Je mag niet gaan stemmen")

# temperatuur = 30
# if temperatuur >= 30:
#     print("Het is warm")
# elif 20 <= temperatuur <= 30:
#     print("Het is aangenaam")
# else:
#     print("Het is koud")

# regen = True
# sneeuw = False
# if regen or sneeuw:
#     print("Het is slecht weer")

# is_oud = False
# if not is_oud:
#     print("De persoon is jong")

# naam = "Sattawat"
# leeftijd = 34

# if leeftijd >= 18:
#     print(f"Hallo, {naam}, je mag autorijden!")
# else:
#     print(f"Hallo, {naam}, je mag nog niet autorijden.") 

# is_zonnig = False
# is_weekend = False

# if is_zonnig or is_weekend:
#     print("Je kunt naar buiten")
# else:
#     print("Het is beter om binnen te blijven")

# aantal_appels = 8
# aantal_bananen = 8
# if aantal_appels > aantal_bananen:
#     print("Meer appels")
# elif aantal_appels == aantal_bananen:
#     print("Evenveel appels en bananen")
# else:
#     print("Meer bananen")

# x = 10
# y = 20
# z = 0
# z += x + y
# print("z =", z)

# if z > 30:
#     print("Te groot!")
# else:
#     print("Dat is in orde")

# is_weer_goed = True
# print("Weer goed (negatief):", not is_weer_goed)

# for i in range(6):
#     print(f"Iteratie nummer {i + 1}")

# count = 0
# while count < 3:
#     print(count)
#     count += 1

# total = 0
# while total <=50:
#     number = int(input("Voer een getal in: "))
#     total += number
# print(f"De totale som is: {total} ")

# for num in range(1, 10):
#     if num % 2 == 0:
#         continue
#     print(num)

# for num in range(1, 20):
#     if num == 15:
#         print("Lus gestopt bij 15")
#         break
#     if num % 2 == 0:
#         continue
#     print(num)

# teams = [["Anna", "Bram"], ["Celine", "David"]]
# for team in teams:
#     for student in team:
#         print(student)

# for i in range(1, 6):
#     print("*" * i)

# def begroeting():
#     print("Hallo, welkom!")
# begroeting()

# def zeg_dag(naam):
#     print(f"Hallo {naam}, fijne dag!")
# zeg_dag("Sophie")

# def bereken_gemiddelde(getallen):
#     if not getallen:
#         return 0
#     return sum(getallen) / len(getallen)
# getallen = [2, 4, 6, 8, 10]
# gemiddelde = bereken_gemiddelde(getallen)
# print(f"Het gemiddelde is : {gemiddelde}")

# def vraag_getallen():
#     getallen = []
#     for _ in range(10):
#         getal = int(input("Geef een getal: "))
#         getallen.append(getal)
#     return getallen

# def bereken_even_gemiddelde(getallen):
#     even_getallen = [x for x in getallen if x % 2 == 0]
#     if even_getallen:
#         gemiddelde = sum(even_getallen) / len(even_getallen)
#     else:
#         gemiddelde = 0
#     return even_getallen, gemiddelde

# def print_kwadraten(lijst):
#     for num in lijst:
#         print(f"Getal: {num}, Kwadraat: {num**2}")

# # Uitvoering
# getallen = vraag_getallen()
# even_getallen, gemiddelde = bereken_even_gemiddelde(getallen)
# print("Even getallen:", even_getallen)
# print("Gemiddelde van even getallen:", gemiddelde)
# print_kwadraten(getallen)

# Release_year = 1990
# Runtime = 2
# rating_out_of_10 = 1.3

# coffee_price = 1.50
# number_of_coffee = 4

# totaal = coffee_price * number_of_coffee
# print(totaal)

# coffee_price = 2
# print(coffee_price * number_of_coffee)

# my_age = 34
# half_my_age = my_age / 2
# greeting = "Hello!"
# name = "Sattawat"
# greeting_with_name = greeting +" " + name
# print(half_my_age)
# print(greeting_with_name)

# user_name = "Sattawat"
# if user_name == "Sattawat":
#     print(f"Get off my computer {user_name}!")
# else:
#     print(f"You can use my computer {user_name}!")

# x = 40
# y = 20
# if x == y:
#     print("Getallen zijn gelijk!")
# else:
#     print("Getallen zijn niet gelijk!")
# credits = 90
# if credits >= 120:
#     print("Je hebt genoeg credits")
# else:
#     print("Je hebt niet genoeg credits")

# # oefening 1 les 2
# a = 10
# b = 20
# som = a + b
# print(f"De waarde is: {som}")
# verschil = a - b
# print(f"De waarde is: {verschil}")
# product = a * b
# print(f"De waarde is : {product}")
# quotient = a / b
# print(f"De waarde is : {quotient}")

# # oefening 3 les 2
# Getal = int(input("Geef een getal in: "))
# if Getal % 2 == 0:
#     print(f"Het getal {Getal} is even!")
# else:
#     print(f"Het getal {Getal} is oneven!")

# #Oefening 4 les 2
# gewicht = float(input("Wat is je gewicht in kg? "))
# lengte = float(input("Wat is je lengte in m? "))
# BMI = gewicht / (lengte * lengte)
# print(f"Mijn BMI is {BMI:.2f}")

# #Oefening 5 les 2
# celsius = float(input("Hoeveel graden celsius is het? "))
# fahrenheit = (celsius * 9 / 5) + 32
# print(f"De temperatuur in {celsius} is gelijk aan {fahrenheit:.2f} in fahrenheit.")

# # Oefening 6 les 2
# prijs = float(input("Wat is de prijs van het product? "))
# korting = prijs * 0.20
# prijs_na_korting = prijs - korting
# print(f"De prijs na korting is {prijs_na_korting}.")

# #Oefening list 1
# sam_height_and_testscore = ["Sam", 67, 85.5, True]
# print(sam_height_and_testscore)

# #Oefening list 2
# orders = ["daisies","periwinkle"]
# orders.append("tulips")
# orders.append("roses")
# print(orders)

# #Oefening 2 lijsten toevoegen (bestaande lijst)
# items_sold = ["cake", "cookie"]
# items_sold_new = items_sold + ["biscuit","tart"]
# print(items_sold_new)

# #Oefening 2de index (3de naam) oproepen in een lijst
# calls = ["sattoe","ine","nils","bom"]
# print(calls[2])

# #Oefening 4de element oproepen in lijst
# studenten = ["Jef","Bram","Joske","Marie"]
# student_vier = studenten[3]
# print(student_vier)

# #oefening laatste element oproepen in de lijst zonder te weten wat het is
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# print(pancake[-1])

# #Oefening vervangen item in lijst door een andere (index gebruiken)
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake[0] = "pokemon eggs"
# print(pancake)

# #Oefening vervangen item met negative index
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake[-1] = "pokemon love"
# print(pancake)

# #Oefening item uit lijst verwijderen
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake.remove("eggs")
# print(pancake)

# #Oefening dubbele item uit lijst verwijderen (enkel eerste dubble item wordt verwijdert)
# pancake = ["eggs","flour","butter","milk","eggs","love"]
# pancake.remove("eggs")
# print(pancake)

# #Oefening met insert() - elementen toevoegen aan een lijst op specifieke index
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake.insert(2, "candy")
# print(pancake)

# #oefening met pop() - verwijderen van een element op een specifieke index
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake.pop(2)
# print(pancake)

# #oefening met pop() - item verwijderen van bestaande lijst naar een nieuwe variabele
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake_delete = pancake.pop(-1)
# print(pancake)
# print(pancake_delete)

# #oefening met pop() - item verwijderen van bestaande lijst naar nieuwe lijst
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake_delete = []
# item = pancake.pop(-2)
# pancake_delete.append(item)
# print(pancake)
# print(pancake_delete)

# #oefening met range() in lijst - gebruiken van list() en range() om opeen volgende getallen 0 - 9 in een lijst weer te geven
# my_range = range(10)
# print(list(my_range))

# #oefening met range()  - lijst bewerken - weergave van range 2 tot 9 (9 niet in begrepen)
# my_list = range(2,9)
# print(list(my_list))

# #oefening met range() - lijst maken die getallen overslaat - dit geef aan dat we binnen de range van 2 tot 9 werken en per 2 overslaat
# my_range2 = range(2,9,2)
# print(list(my_range2))

# #Oefening met range() - zelfde maar groter getallen
# my_range_3 = range(0,100,4)
# print(list(my_range_3))

# #Oefening met len() - lengte van een lijst weergeven (aantal item in de lijst)
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# print(len(pancake))

# #Oefening met len() - weergeven van gemixte variabelen in een lijst en 2 lijsten - output is lengte van lijst weergeven
# long_list = [1,5,6,7,-23,69.5,True,"very","long","list","that","keeps","going","Let's","practice","getting","the","length"]
# big_list = range(2,3000,10)

# long_list_len = len(long_list)
# print(long_list_len)

# big_range_length = len(big_list)
# print(big_range_length)

# #Oefening slechts een deel van lijst extraheren - slicing - eerste index tot 6de index, 0 werd weggelaten)
# letters = ["a","b","c","d","e","f","g"]
# sliced_list = letters[1:6]
# print(sliced_list)

# #Oefening eerste 3 item van de lijst weergeven of selecteren - dubbelepunt VOOR de selectie aantal item heel belangrijk!!
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# print(pancake[:3])

# #Oefening laatste 2 item van lijst weergeven of selecteren - dubbelepunt NA de selectie aantal item heel belangrijk!!
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# print(pancake[-2:])

# #Oefening alle item uitgezonderd de laatste
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# print(pancake[:-1])

# #Oefening met count() - tellen hoeveel keer een bepaalde item in de lijst voorkomt
# letters = ["a","b","c","d","e","f","g","a","b","c","d","e","f","g","a","b","c","d","e","f","g" ]
# num_letters = letters.count("a")
# print(num_letters)

# #Oefening met sort() - sorteren van strings in alfabetische volgorde
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake.sort()
# print(pancake)
# #Oefening met sort() - sorteren van strings in OMGEKEERDE alfabetische volgorde
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# pancake.sort(reverse=True)
# print(pancake)

# #oefening met sort() - sorteren van int/float in numerieke volgorde
# getallen = [63,56,98,6,36.5,7,22.69,96.87,16]
# getallen.sort()
# print(getallen)
# #oefening met sort() - sorteren van int/float in OMGEKEERDE numerieke volgorde
# getallen = [63,56,98,6,36.5,7,22.69,96.87,16]
# getallen.sort(reverse=True)
# print(getallen)

# #Oefeningen met sorted() - let op! niet zelfde als sort() - sorted maak een nieuwe lijst aan in alfabetische orde
# names = ["Sattawat", "Ine", "Elena", "Celeste", "Shiro"]
# sorted_names = sorted(names)
# print(sorted_names)

# Oefening 1
# getallen = []
# getallen.append(1)
# getallen.append(2)
# getallen.append(3)
# getallen.append(4)
# getallen.append(5)
# getallen.pop(2)
# print(f"Lijst na het verwijderen van het derde element: {getallen}")

#Oefening 2
# names = ["Sattawat", "Ine", "Elena", "Celeste", "Shiro","Alice"]
# names.remove("Alice")
# print(f"Hier een aangepaste namenlijst : {names}")

#Oefening 3
# getallen = [96,52,63,12,70,23,58,99]
# getallen.sort()
# print(f"Hier een lijst van gesorteerde getallen : {getallen}")

#oefening 4
# nummers = []
# nummers.append(1)
# nummers.append(2)
# nummers.append(3)
# nummers.append(4)
# nummers.append(5)
# nummers.pop(2)
# nummers.insert(1,6)
# nummers.remove(2)
# print(f"Lijst na bewerking : {nummers}")

#Oefening 5
# number_list = [1,2,3,4,5]

# if number_list[0] % 2 == 0:
#     print(f"Even getal: {number_list[0]}")
# else:
#     print(f"Oneven getal: {number_list[0]}")

# if number_list[1] % 2 == 0:
#     print(f"Even getal: {number_list[1]}")
# else:
#     print(f"Oneven getal: {number_list[1]}")

# if number_list[2] % 2 == 0:
#     print(f"Even getal: {number_list[2]}")
# else:
#     print(f"Oneven getal: {number_list[2]}")

# if number_list[3] % 2 == 0:
#     print(f"Even getal: {number_list[3]}")
# else:
#     print(f"Oneven getal: {number_list[3]}")

# if number_list[4] % 2 == 0:
#     print(f"Even getal: {number_list[4]}")
# else:
#     print(f"Oneven getal: {number_list[4]}")

#Oefening 6
# numbers = [10,6,36,8,90]
# if numbers[0] > 10:
#     print(f"Groter dan 10: {numbers[0]}")
# else:
#     print(f"Kleiner dan 10: {numbers[0]}")

# if numbers[1] > 10:
#     print(f"Groter dan 10: {numbers[1]}")
# else:
#     print(f"Kleiner dan 10: {numbers[1]}")

# if numbers[2] > 10:
#     print(f"Groter dan 10: {numbers[2]}")
# else:
#     print(f"Kleiner dan 10: {numbers[2]}")

# if numbers[3] > 10:
#     print(f"Groter dan 10: {numbers[3]}")
# else:
#     print(f"Kleiner dan 10: {numbers[3]}")

# if numbers[4] > 10:
#     print(f"Groter dan 10: {numbers[4]}")
# else:
#     print(f"Kleiner dan 10: {numbers[4]}")

#oefening 7
# steden = ["Amsterdan","New York","Parijs","London","Tokio"]
# steden.pop(2)
# steden.insert(1,"Berlijn")
# steden.remove("New York")
# print(f"Hier de aangepaste steden lijst: {steden}")

# Oefening 8
# punten = [85,92,78,90,88,76,89,95,80]

# punten.append(84)
# punten.remove(76)
# punten.insert(2,91)
# punten.sort()
# print(f"Hier is de lijst met punten : {punten}")
# gemiddelde = sum(punten) / len(punten)
# print(f"Het gemiddelde is: {gemiddelde}")

# if punten[-1] > 90:
#     punten[0] += 5
#     punten[1] += 5
#     punten[2] += 5
#     punten[3] += 5
#     punten[4] += 5
#     punten[5] += 5
#     punten[6] += 5
#     punten[7] += 5
#     punten[8] += 5
#     punten[9] += 5
# print(punten)

# uiteindelijke_gemiddelden = sum(punten) / len(punten)
# raad = float(input("Raad het gemiddelde: "))
# if raad == uiteindelijke_gemiddelden:
#     print(f"Proficat, dit is correct, het gemiddelde is: {uiteindelijke_gemiddelden}")
# else:
#     print(f"Helaas, dit is niet correct, het gemiddelde is: {uiteindelijke_gemiddelden}")

# Loops

# For loops
#lijst met ingredienten apart afdrukken
# pancake = ["eggs","flour","butter","milk","sugar","love"]

# for ingredient in pancake:
#     print(ingredient)

#Oefening - print elke element uit board_games lijst, gebruik een for loop
# board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]
# sport_games = ["football", "hockey", "baseball", "cricket"]

# for board in board_games:
#     print(board)

# for sport in sport_games:
#     print(sport)

#oefening - range() functie
# six_steps = range(6)
# for steps in six_steps:
#     print(steps)

#oefening met rang() functie learing loops
# for temp in range(6):
#     print("Learning Loops!")

#oefening het bijhouden van aantal range() - index begin met 0 dus moeten wij +1 zetten - str() = string()
# for temp in range(6):
#     print("Loop is on iteration number " + str(temp + 1))

# While loops
#Oefening met while loop - gehele getallen 0 tot en met 3 afdrukken - zonder count +=1 op het einde, blijft het oneinig doorlopen
# count = 0
# while count <= 3:
#     print(count)
#     count += 1

#oefening met while - in een lijst itereren
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# length = len(pancake)
# index = 0
# while index < length:
#     print(pancake[index])
#     index += 1

#Oefening - doorzoeken van een lijst
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# for ingredient in pancake:
#     if ingredient == "milk":
#         print("Found it")

#Oefening - loop control - break - stoppen met zoeken na dat je item gevonden hebt
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# print("Checking the ingredients!")
# for ingredient in pancake:
#     print(ingredient)
#     if ingredient == "milk":
#         break
# print("End of search!")

#Oefening loop control - continue - iteratie van lus overslaan bij negatieve getallen - enkel positieve getallen weergeven 
# numbers = [1,2,-1,4,-5,5,2,-9]
# for num in numbers:
#     if num <= 0: 
#         continue
#     print(num)

#Nested loops

#Oefening nested loops - printen van teams in de lijst - [[]] = lijst in een lijst (nested list)
# project_teams = [["Ava", "Samanta","James"], ["Lucille","Zed"], ["Edgar","Gabriel"]]
# for team in project_teams:
#     print(team)

#Oefening nested loops - printen van nested list als individueel - lussen moeten nesten om elke sublijst te kunnen lussen
# project_teams = [["Ava", "Samanta","James"], ["Lucille","Zed"], ["Edgar","Gabriel"]]
# for team in project_teams: 
#     for student in team: #door de sublijst lussen
#         print(student)

# sport_teams = [["Mila","Noah","Oliver"],["Sophia","Liam","Ethan"],["Isabella","Mason","Emma"]]
# team_names = ["Team A", "Team B", "Team C"]

# for index, team in enumerate(sport_teams):
#     print(f"{team_names[index]}:")
#     for player in team:
#         print(f" - {player}")

#Oefening: 1) maak lijst met 0-9 (incl 9) 2) maak for-lus door single_digit en druk elk cijfer af
# 3) lijst maken met squares, wijs lege lijst aan toe 4) binnen de lust door single_digits de dubbele waarde  van elk element toe aan lijst squares
# 5) druk squares af
# single_digits = range(10)
# squares = []

# for digit in single_digits:
#     print(digit)
#     squares.append(digit * 2)
# print(squares)

# Oefening met ster tot patroon ster 5
# for ster in range(1,6):
#     print(ster * "*")

# Oefening omgekeerde patroon ster 5
# for ster in range(5,0,-1): #start bij 5 en eindigd bij 1
#     print(ster * "*")

# oefening driehoekig patroon met spaties:
# for ster in range(1,6):
#     print(" " * (5 - ster) + "*" * ster)
# " " * (5 - ster) creëert een string met een aantal spaties gelijk aan 5 - ster
#Als ster = 1, dan krijg je 5 - 1 = 4 spaties.
#Als ster = 2, dan krijg je 5 - 2 = 3 spaties.
#Dit patroon gaat door tot ster = 5, waarbij er geen spaties meer zijn (5 - 5 = 0).

#Functies

#Oefening fucntie oproepen
# def directions_to_timesSq():
#     print("Walk 4 min to 34th St Herald Square train station.")
#     print("Take the Northbound N, Q, R, or W train 1 stop.")
#     print("Get off the Times Square 42nd Street stop.")
# directions_to_timesSq()

#Oefening functie oproepen, uitbreiding - voeg meer stappen of keuzes toe
# def directions_to_timesSq():
#     print("Option 1: Walk 4 min to 34th St Herald Square train station.")
#     print("Take the Northbound N, Q, R, or W train 1 stop.")
#     print("Get off the Times Square 42nd Street stop.")
#     print("Option 2: Take a taxi directly to Times Square.")
# directions_to_timesSq()

#Oefening functie oproepen, interactie - Laat gebruiker kiezen hoe ze naar TSq willen reizen
# def directions_to_timesSq():
#     choice = input("Do you prefer train (1) or taxi (2)? ")
#     if choice == "1":
#         print("Walk 4 min to 34th St Herald Square train station.")
#         print("Take the Northbound N, Q, R, or W train 1 stop.")
#         print("Get off the Times Square 42nd Street stop.")
#     elif choice == "2":
#         print("Take a taxi directly to Times Square.")
#     else:
#         print("Invalid choice. Please try again.")
# directions_to_timesSq()

#Oefening - functie oproepen - als je niet laat uitlijnen in de fuctie en je roept het op komt de print fuctie (niet insprong) eerst
# def trip_welcome():
#     print("Welcome to Tripcademy!")
#     print("Let's get you to your destination.")
# print("Woah, look at the weather outside! Don't walk, take the train!")
# trip_welcome()

#Oefening - Functie
# print("We zullen het weer voor jou controleren!")

# def weather_check():
#     print("Het is een mooie dag om te reizen!")
#     print("Het regent! Best niet reizen!")
# weather_check()

#Oefening - parameters en argumenten
# def trip_welcome(destination): #tijdelijke variabele aanmaken
#     print("Welcome to Tripcademy!")
#     print("Looks like you're going " + destination + " today") #tijdelijke variabele ingeven
# trip_welcome("Times Squares") #parameter meegeven

#Schrijf een programma dat de gebruiker vraagt om 10 gehele getallen in te voeren.
# Het programma moet alle even getallen in een lijst plaatsen, vervolgens het gemiddelde van deze even getallen berekenen en afdrukken.
# getallen_lijst = []

#my way
# for getal in range(1,11):
#      getal = int(input("Voer een getal in: "))
#      if getal % 2 == 0:
#          getallen_lijst.append(getal)
#          gemiddelde = sum(getallen_lijst) / len(getallen_lijst)
# print(f"Het gemiddelde van de even getallen lijst is : {gemiddelde:.2f}") # twee cijfers na de komma is :.2f

# even_getallen = []
# for i in range(10):
#     getal = int(input("Voer een getal in: "))
#     if getal % 2 == 0:
#         even_getallen.append(getal)
# if even_getallen:
#     gemiddelde = sum(even_getallen) / len(even_getallen)
#     print(f"Het gemiddelde van de lijst is : {gemiddelde:.2f}")
# else:
#     print("Er zijn geen even getallen ingevoerd!")

#Schrijf een programma dat lijst met getallen aanmaakt en vervolgens alle even filtert afdrukt. Gebruik for-lus om door de te itereren if-statement identificeren.
# getallen_lijst = [10,36,55,99,87,63,70]
# print(f"Originele lijst : {getallen_lijst}")
# even_getallen = []
# for getal in getallen_lijst:
#     if getal % 2 == 0:
#         even_getallen.append(getal)
# print(f"Hier is een lijst met de even getallen: {even_getallen}")

# getallen_lijst = [10,36,55,99,87,63,70]
# print("Originele lijst: ", getallen_lijst)

# even_getallen = []
# for getal in getallen_lijst:
#     if getal % 2 == 0:
#         even_getallen.append(getal)
# print(f"Even getallen : {even_getallen}")

#Oefening: even getallen telt tussen 1 en 20. Gebruik een for-lus voor eerste 10 getallen en while lus voor resterende 10 getallen.
#continue om de iteratie over te slaan als het getal deelbaar is door 3 en gebruik break om de lus te verlaten als het getal 17 is.
# even_getallen_for = 0

# for number in range(1,11):
#     if number % 3 == 0:
#         continue
#     if number % 2 == 0:
#         even_getallen_for += 1

# even_getallen_while = 0
# nummer = 11

# while nummer <= 20:
#     if nummer == 17:
#         break
#     if nummer % 3 == 0:
#         nummer += 1
#         continue
#     if nummer % 2 == 0:
#         even_getallen_while += 1
#     nummer += 1

# print(f"Getallen door de for loop: {even_getallen_for}")
# print(f"Getallen door de while loops: {even_getallen_while}")

#Oefening - getallen optellen tot aan een grens: variabele totaal initialiseert met 0 en gebruikers telkens vraagt in te voeren.
#           Blijf de ingevoerde getallen optellen met totaal zolang de som onder de 100 blijft. Stop de lus zodra totaal 100 bereikt of oveschrijdt en druk dan het eindtotaal af.

# totaal = 0

# while totaal < 100:
#     getallen = int(input("Voer een getal: "))
#     totaal += getallen
#     print(f"Huidige totaal is {totaal}")
# print(f"Lus is gestopt! Het totaal is {totaal}")

#oefening -Vroegtijdige beëindiging van een lus: Schrijf programma dat lijst bevat willekeurige getallen tussen 1 en 20. Gebruik for-lus om elk getal af te drukken. Als het 13 is, beëindig dan de lus met break en druk waarschuwing af dat het getal 13 is gevonden. 
# getallen = [10,13,16,8,6,11,20,]
# for getal in getallen:
#     print(getal)
#     if getal == 13:
#         print("Het getal is gevonden!")


#STRING METHODES

#Oefening met .lower() , .upper() , .title()
# song = 'sMooTh'
# print(song.lower())
# print(song.upper())
# print(song.title())

#oefening strings splitten
# tekst = "Hallo ik ben Sattawat Beernaert"
# resultaat = tekst.split()
# print(resultaat)

# tekst = "appel,peren,bannan"
# resultaat2 = tekst.split(",")
# print(resultaat2)

# tekst = "Hallo ik ben Sattawat Beernaert"
# resultaat3 = tekst.split(" ",3)
# print(resultaat3)

# tekst = "Hallo ik ben Sattawat Beernaert"
# resultaat4 = tekst.split(",")
# print(resultaat4)

#Oefening string splitsen bij een letter
# name = "Sattawat"
# print(name.split("a"))

#Oefening samenvoegen van lijst van strings
# woorden = ["Hallo", "wereld", "dit", "is", "Python"]
# resultaat = " ".join(woorden)
# print(resultaat)

# items = ["appel", "banaan", "kers"]
# resultaat = ", ".join(items)
# print(resultaat)

# woorden = ["2024", "11", "25"]
# resultaat = "-".join(woorden)
# print(resultaat)

# letters = ["P", "Y", "T", "H", "O", "N"]
# resultaat = "".join(letters)
# print(resultaat)

# oefening modules - random nummers generen tussen 1 en 100

# import random #import random below
# random_list = [random.randint(1,100) for i in range(101)] # willekeurig lijst aanmaken
# random_nummer = random.choice(random_list) #random nummer aanmaken
# print(random_nummer)

#Oefening - Maak een functie ‘to_uppercase’ die string als parameter verwacht. Deze zal de omzetten naar hoofdletters. Maak een functie ‘to_uppercase’ die string als parameter verwacht. Deze zal de omzetten naar hoofdletters. Maak
# def to_uppercase(text):
#     return text.upper()
# input_str = "dit is een voorbeeld" #defineer een statische string
# output_str = to_uppercase(input_str) #omzetten van string naar hoofdletters
# print(output_str)

#Dictionary

#oefening - woordenboek aanmaken met keys en values
#menu met gerechten erin en hun prijzen
# menu = {"pizza":7, "pita":5, "spaghetti":10, "frietjes": 4}
# print(menu)
#Oefening - woordenboek aanmaken met enkel getallen
# totaal = {24:20, 25:21, 36:40}
# print(totaal)

#oefening - woordenboek maken genaamd vertalingen en koppelt de engelse woorden aan de elventaal en print het uit
# vertalingen = {"mountain":"orod", "bread":"bass", "friend":"mellon", "horse":"roch" }
# print(vertalingen)

#oefening - lege woordenboek maken
# empty_dict = {}

#Oefening - sleutel en waarde toevoegen aan een lijst
# menu = {"pizza":7, "pita":5, "spaghetti":10, "frietjes": 4}
# menu["hamburber"] = 6
# print(menu)

#oefening - lege wooordenboek maken animal_zoo
#toevoegen : zebra's met waarde 8, apen waarde 12, dino waarde 0
# animal_zoo = {}
# animal_zoo["zebra's"] = 8
# animal_zoo["apen"] = 12
# animal_zoo["dino"] = 0
# print(animal_zoo)

#oefening meerdere keys toevoegen aan je woordenboek
# menu = {"pizza":7, "pita":5, "spaghetti":10, "frietjes": 4}
# menu.update({"hamburger":6, "kip": 8})
# print(menu)

#oefening - overschijven van waarden
# menu = {"pizza":7, "pita":5, "spaghetti":10, "frietjes": 4}
# menu["pita"] = 6 #waarden hierboven van de pita wordt aangepast naar 6
# menu["pizza"] = 8 #sleutel van de pizz wordt aangepast naar 8
# print(menu)

#oefening - 2 lijsten combineren in een woordenboek
# pancake = ["eggs","flour","butter","milk","sugar","love"]
# prijs = [3,2,5,4,9,0]
# store = {key:value for key, value in zip(pancake,prijs)} #zip() 2 lijsten combineren tot een iterator die lijsten aan elkaar koppelt
# print(store)

#oefening - keys uit een woordenboek halen
# menu = {"pizza":7, "pita":5, "spaghetti":10, "frietjes": 4}
# print(menu["pizza"])
# print(menu["spaghetti"])

#oefening - waarde oproepen met .get()
# menu = {"pizza":7, "pita":5, "spaghetti":10, "frietjes": 4}
# print(menu.get("pizza"))
# print(menu.get("hamburger")) #hamburger staat niet in woordenboek dus zal het return non zijn.

#oefening - waarde retourneren ipv none maar als nieuwe waarde of strings
# menu = {"pizza":7, "pita":5, "spaghetti":10, "frietjes": 4}
# print(menu.get("pizza",0))
# print(menu.get("hamburger","Niet op de menu!"))

#oefening - keys verwijderen met .pop - telkens juiste nummer wordt ingegeven wordt het uit de woordenboek verwijdert
# raffle = {13215:"Teddy Bear", 65412:"Concert Tickets", 69745:"Gift Basket", 65214:"Necklace"}

# print(raffle.pop(13215, "No prize"))
# print(raffle.pop(10000, "No prize"))
# print(raffle)
# print(raffle.pop(65412,"No Prize"))
# print(raffle)

#oefening - alle keys oproepen - enkel leerlingen oproepen in lijst en individueel
# test_scores = {"Sat": [80,72,90], "Ine": [88,68,81], "Elena":[80,82,84], "Celeste": [98,96,95]}
# print(list(test_scores)) # lijst oproepen met enkel de keys (leerlingen)
# for student in test_scores.keys(): #weergeven individueel
#     print(student)

# #oefening - alle values oproepen - enkel scores oproepen in lijst en individueel
# for score_list in test_scores.values(): # scores weergeven in lijstvorm
#     print(score_list)
# for student in test_scores.keys(): # studenten oproepen individueel
#     print(student)

#oefening - get all keys
#1) dict maken met naam auto - volgende paren: merk:toyota, model:corolla,jaar:2022,kleur:blauw
#2)jaar uit dict verwijderen 3) brandstof op te halen - geef 'niet gespecifeerd' als fallback
#4)druk aangepast dict af 5) druk verwijderde waarde jaar af 6) druk resultaat van de get-methode af voor brandstof

# auto = {"merk":"Toyota", "model":"corolla", "jaar": 2022, "kleur":"blauw"}
# deleted_list = auto.pop("jaar", None)
# brandstof = auto.get("brandstof","Niet gespecificeerd")
# auto.get("brandstof", "Niet gespecificeerd")
# print(f"Dit is de aangepaste lijst van auto: {auto}")
# print(f"Verwijderde jaartal : {deleted_list}")
# print(f"brandstof? {brandstof}")

# oefening - alle waarden oproepen met .values()
# menu = {"pizza":7, "pita":5, "spaghetti":10, "frietjes": 4}
# waarde_menu = menu.values()
# print(waarde_menu)

# waarde_menu_list = list(menu.values()) #weergeven in lijstvorm
# print(waarde_menu_list)

#Bestanden

#oefening - bestanden lezen met.read() - read() leest het hele bestand als één enkele string
#Er moet al een tekst bestand zitten in je mapje met inhoud erin!! Je moet in de juiste map aan het werken zijn of veranderen van pad met :
#cd pad\naar\je\map

# with open("real_cool_document.txt") as cool_doc:
#     cool_contents = cool_doc.read()
# print(cool_contents)

#Oefening bestanden lezen met readlines() - readlines() het bestand leest en elke regel als een apart element in een lijst plaatst.
# with open("Voorbeeld.txt") as voorbeeld_doc:
#     for line in voorbeeld_doc.readlines():
#         print(line)

#Oefening bestanden lezen met .readline() - enkel zinnen tonen die je wilt
# with open("Voorbeeld.txt") as voorbeeld_doc:
#     first_line = voorbeeld_doc.readline()
#     second_line = voorbeeld_doc.readline()
#     print(first_line)

# oefening bestanden maken - Let op maak bestand aan in het mapje dat je nu bevindt!!
# with open("generated_file.txt", "w") as gen_file: #maken van het bestand genaamd ....txt, de "W" staat voor write
#     gen_file.write("What an incredible file") # tekst in het bestand zetten - indien al bestand bestaat wordt het overgeschreven

# with open("generated_file.txt") as gen_doc:
#     gen_content = gen_doc.readlines()
#     print(gen_content)

#Oefening - regel toevoegen aan bestand zonder over te schrijven of verwijderen
# generated_file bij werken - a van append
# with open("generated_file.txt", "a") as gen_file:
#     gen_file.write("\n... and it still is") #"\n = nieuwe lijn beginnen

#oefening - bestand maken en tekst inzetten
# with open("fun_cities_file.txt", "w") as fun_cities_doc:
#     fun_cities_doc.write("Montreal")

#oefening - sluiten van bestandsverbinding
# with open("fun_cities_file.txt", "a") as fun_cities_doc:
#     fun_cities_doc.write("\nTokyo")
#     fun_cities_doc.close()
#     fun_cities_doc.write("n\LA")

#oefening - CSV-bestand lezen - Eer csv bestand maken of in je mapje hebben!
# import csv #De csv module wordt geïmporteerd om het lezen van CSV-bestanden eenvoudiger te maken.

# list_of_email_adresses = [] # legelijst maken om later email adressen in te steken
# with open("users.csv", newline="") as users_csv: #Het bestand users.csv wordt geopend in leesmodus (r) & De newline="" parameter voorkomt extra lege regels die kunnen ontstaan bij het lezen van CSV-bestanden op sommige systemen (zoals Windows).
#     user_reader = csv.DictReader(users_csv) #csv.DictReader leest het CSV-bestand en behandelt elke rij als een dictionary waarbij de kolomnamen van het CSV-bestand worden gebruikt als sleutels.
#     for row in user_reader: #Een for-lus wordt gebruikt om door elke rij in het bestand te itereren. Elke rij wordt als een dictionary (row) behandeld.
#         list_of_email_adresses.append(row["Email"]) #Hier wordt de waarde die overeenkomt met de sleutel "Email" uit de dictionary (de rij) gehaald en toegevoegd aan de lijst list_of_email_adresses.
# print(list_of_email_adresses)

#Oefening

# import csv

# with open("users.csv", newline="") as users_csv:
#     users_reader = csv.DictReader(users_csv,delimiter=",")
#     for row in users_reader:
#         print(row["Name"])

#Oefening csv bestand maken (writing)
# big_list = [{'name': 'Sattawat Beernaert', 'userid': 12345, 'is_admin' : False}, {'name': 'Ine Dupont', 'userid': 56789, 'is_admin' : True}]

# import csv

# with open("new-users.csv", "w") as new_csv: # nieuwe csv bestand aanmaken met naam new-user.csv in schrijfmodus "w"
#     fields = ['name', 'userid', 'is_admin'] #Dit is een lijst met de namen van de kolommen (de header) die in het CSV-bestand zullen worden opgenomen.
#     new_writer = csv.DictWriter(new_csv, fieldnames=fields) #object wordt aangemaakt om rijen in het CSV-bestand te schrijven.

#     new_writer.writeheader() #Deze methode schrijft de header (de kolomnamen) naar het bestand. Dit zorgt ervoor dat de eerste regel in het CSV-bestand de kolomnamen bevat: name,userid,is_admin.
#     for item in big_list: #Hier wordt aangenomen dat big_list een lijst van dictionaries is, waarbij elke dictionary gegevens bevat die overeenkomen met de kolommen name, userid, en is_admin.
#         new_writer.writerow(item) # schrijf in 1 rij naar bestand overeenkomt met fieldnames

#Oefening Json bestand lezen - json bestand moet in je map zitten!!

# import json

# with open("leerling.json") as leerling_json:
#     leerling_reader = json.load(leerling_json)

# print(leerling_reader["naam"])

#oefening Json bestand schrijven
# import json

# with open("output.json", "w") as json_file:
#     json.dump("turn_to_json", json_file)

#Oefening - 
# getallen = {5:1, 10:2, 15:3, 20:4, 25:5}
# verwijderd = getallen.pop(25)
# print(f"Aangepaste dict: {getallen}")
# gevonden = getallen.get(25, "Niet gevonden")
# print(f"getallen opnieuw halen: {gevonden}")

# -Oefening - gemiddelde berekenen per student 
# cijfers = {"Sattawat": [80,81,82], "Ine": [83,84,85], "Elena": [86,87,88], "Celeste": [89,90,91]}
# for naam, lijstpunten in cijfers.items():
#     gemiddelde = sum(lijstpunten) / len(lijstpunten)
#     print(f"De student {naam} heeft een gemiddelde cijfer van {gemiddelde:.2f}")

# studenten = [{"naam":"Sattawat", "cijfer": 7.5}, {"naam":"Ine", "cijfer":8.0}]

# import csv

# with open("studenten.csv", "w") as studenten_csv:
#     fields = ["naam","cijfer"]
#     studenten_writer = csv.DictWriter(studenten_csv, fieldnames=fields)
#     studenten_writer.writeheader()

#     for item in studenten:
#         studenten_writer.writerow(item)

# with open("mijn_notities.txt", "w") as notities_txt:
#     notities_txt.write("Hallo.\n")
#     notities_txt.write("ik.\n")
#     notities_txt.write("Sattawat.\n")

# with open("mijn_notities.txt", "a") as notities_txt:
#     notities_txt.write("Bye Bye\n")

# with open("mijn_notities.txt", "r") as notities_txt:
#     inhoud = notities_txt.read()
#     print(inhoud)

#Oefening - schrijf een programma dat de frequentie van elke letter in een opgegeven woord telt.
# woord = input("Voer een woord in: ")
# frequentie = {}

# for letter in woord:
#     if letter in frequentie:
#         frequentie[letter] += 1
#     else:
#         frequentie[letter] = 1

# print("Frequentie van elke letter: ")
# for letter, count in frequentie.items():
#     print(f"{letter} in {count}")

#oefening winkelwagentje en totaal berekenen

# # Winkelkarretje dictionary
# Winkelkarretje = {}

# # Vraag de gebruiker om producten en prijzen toe te voegen
# while True: #oneindig lus (toevoegen)
#     product = input("Voer een product in (of 'stop' om te stoppen): ")
#     if product.lower() == 'stop':
#         break #lus stoppen, hier door "stop" in te voeren
#     prijs = float(input(f"Voer de prijs in voor {product}: "))
#     Winkelkarretje[product] = prijs

# # Bereken het totaal
# Totaal = sum(Winkelkarretje.values())

# # Print het totaal van het winkelkarretje
# print(f"Het totaal van de winkelkar is: €{Totaal:.2f}")

# # Toon een overzicht van het winkelkarretje
# print("\nOverzicht van je winkelkarretje:")
# for product, prijs in Winkelkarretje.items():
#     print(f"{product}: €{prijs:.2f}")

# # Print het totaalbedrag
# print(f"\nHet totaal van de winkelkar is: €{Totaal:.2f}")

# Winkelwagen met keuze-menu's

# winkelwagen = {}

# def toon_winkelwagen(winkelwagen):
#     """Functie om de inhoud van het winkelwagentje te tonen."""
#     if not winkelwagen:
#         print("Je winkelwagentje is leeg.")
#     else:
#         print("\nInhoud van je winkelwagentje:")
#         totaal = 0
#         for item, prijs in winkelwagen.items():
#             print(f"- {item}: €{prijs:.2f}")
#             totaal += prijs
#         print(f"Totaal: €{totaal:.2f}")

# print("Welkom in het winkelprogramma!")
# while True:
#     print("\nWat wil je doen?")
#     print("1. Item toevoegen")
#     print("2. Winkelwagentje bekijken")
#     print("3. Afrekenen en stoppen")

#     keuze = input("Voer je keuze in (1, 2, 3): ")

#     if keuze == "1":
#         item = input("Voer de naam van het item in: ")
#         try:
#             prijs = float(input(f"Voer de prijs van {item} in: €"))
#             if prijs < 0:
#                 print("De prijs kan niet negatief zijn. Probeer opnieuw.")
#                 continue
#             winkelwagen[item] = prijs  # Correcte manier om een item toe te voegen
#             print(f"{item} is toegevoegd aan je winkelwagentje voor €{prijs:.2f}")
#         except ValueError:
#             print("Ongeldige invoer voor prijs. Probeer opnieuw.")

#     elif keuze == "2":
#         toon_winkelwagen(winkelwagen)

#     elif keuze == "3":
#         toon_winkelwagen(winkelwagen)
#         print("\nBedankt voor je aankoop! Tot ziens.")
#         break

#     else:
#         print("Ongeldige keuze. Probeer opnieuw.")

#oefening - getal raden tussen 1 en 100

# import random

# def raad_het_getal():
#     geheim_getal = random.randint(1,100)
    
#     print("Welkom bij 'Raad het getal'!")
#     print("Ik heb een getal gekozen tussen 1 en 100. Kun jij het raden?")

#     while True:
#         try:
#             gok = int(input("Voer je gok in: "))
#             if gok < geheim_getal:
#                 print("Hoger")
#             elif gok > geheim_getal:
#                 print("Lager!")
#             else:
#                 print(f" Gefeliciteerd! Je hebt het juiste getal geraden: {geheim_getal}")
#                 break
#         except ValueError:
#             print("Voer alstublief een geldig getal in.")

# raad_het_getal()

#Winkelwagentje waarin prijzen worden opgeslagen. voeg een funtie toe waarmee een korting van 10% wordt toegepast op het totaal bedrag als de waarde meer €50.

# Winkelwagen met automatische korting en geen keuze-menu

# winkelwagen = {}

# def toon_winkelwagen(winkelwagen):
#     """Functie om de inhoud van het winkelwagentje te tonen."""
#     if not winkelwagen:
#         print("Je winkelwagentje is leeg.")
#     else:
#         print("\nInhoud van je winkelwagentje:")
#         totaal = 0
#         for item, prijs in winkelwagen.items():
#             print(f"- {item}: €{prijs:.2f}")
#             totaal += prijs
#         print(f"Totaal zonder korting: €{totaal:.2f}")

#         # Bereken korting als het totaal > €50 is
#         totaal = pas_korting_toe(totaal)
#         print(f"Totaal na eventuele korting: €{totaal:.2f}")

# def pas_korting_toe(totaal):
#     """Functie om korting toe te passen als het totaal > €50 is."""
#     if totaal > 50:
#         korting = totaal * 0.10
#         print(f"Een korting van 10% wordt toegepast: €{korting:.2f}")
#         return totaal - korting
#     return totaal

# print("Welkom bij de winkel!")
# print("Typ 'klaar' om af te rekenen of 'bekijk' om het winkelwagentje te bekijken.\n")

# while True:
#     actie = input("Voeg een item toe (of typ 'klaar' / 'bekijk'): ").strip().lower()

#     if actie == "klaar":
#         toon_winkelwagen(winkelwagen)
#         print("\nBedankt voor je aankoop! Tot ziens.")
#         break

#     elif actie == "bekijk":
#         toon_winkelwagen(winkelwagen)

#     else:
#         # Voeg een nieuw item toe
#         item = actie
#         try:
#             prijs = float(input(f"Voer de prijs van {item} in: €"))
#             if prijs < 0:
#                 print("De prijs kan niet negatief zijn. Probeer opnieuw.")
#                 continue
#             winkelwagen[item] = prijs
#             print(f"{item} is toegevoegd aan je winkelwagentje voor €{prijs:.2f}")
#         except ValueError:
#             print("Ongeldige invoer voor prijs. Probeer opnieuw.")

#Oefening tafelsom genereren bv 6x7 =?
#bij juist zegt correct en fout helaas - 5 pogingen indien 6 toont antwoord

# import random

# def genereer_tafelsommen():
#     print("Welkom bij de tafelsommen quiz!")

#     for poging in range(1,6):
#         getal1 = random.randint(1,10)
#         getal2 = random.randint(1,10)
#         correct_antwoord = getal1 * getal2

#         print(f"Poging {poging}: Wat is {getal1} X {getal2}?")
#         antwoord = input("Jouw antwoord: ")

#         if antwoord.isdigit():
#             antwoord = int(antwoord)
#         else:
#             print("Ongeldige invoer. Probeer opnieuw met een getal.")
#             continue

#         if antwoord == correct_antwoord:
#             print("Correct!")
#             return
#         else:
#             print("Helaas, dat is niet correct.")

# print(f"Het juiste antwoord was: {correct_antwoord}")

# genereer_tafelsommen()

# import random

# def genereer_tafelsommen():
#     print("Welkom bij de tafelsommen quiz!")
#     fouten = 0

#     getal1 = random.randint(1, 10)
#     getal2 = random.randint(1, 10)
#     correct_antwoord = getal1 * getal2

#     for poging in range(1, 6):
#         print(f"Poging {poging}: Wat is {getal1} X {getal2}?")
#         antwoord = input("Jouw antwoord: ")

#         if antwoord.isdigit():
#             antwoord = int(antwoord)
#         else:
#             print("Ongeldige invoer. Probeer opnieuw met een getal.")
#             fouten += 1
#             continue

#         if antwoord == correct_antwoord:
#             print("Correct! Goed gedaan!")
#             return
#         else:
#             print("Helaas, dat is niet correct.")
#             fouten += 1

#     # Na 5 pogingen toon je het juiste antwoord
#     print(f"Je hebt al je pogingen gebruikt. Het juiste antwoord was: {correct_antwoord}")

# # Start de quiz
# genereer_tafelsommen()

#sterren in row
# def print_stars_pattern(rows):
#     for i in range(1, rows + 1):
#         print("*" * 1)
# num_rows = 5
# print(f"Sterretjes patroon met {num_rows} rijen:")
# print_stars_pattern(num_rows)

#oefening countdown!

# def countdown(n):
#     while n > 0:
#         print(n)
#         n -= 1
#     print("Lancering!")

# countdown(5)

#functie die evengetallen geven met limiet

# def print_even_numbers(limit):
#     number = 2
#     while number <= limit:
#         print(number)
#         number += 2

# print_even_numbers(20)

# Oefening getallen van 1 tot 50 afdrukken in veelvoud 3 = fizz, veelvoud 5 = buzz, zowel 3 als 5 fizzbuzz
# def fizzbuzz():
#     for i in range(1,51):
#         if i % 3 == 0 and i % 5 == 0:
#             print("FizzBuzz")
#         elif i % 3 == 0:
#             print("Fizz")
#         elif i % 5 == 0:
#             print("Buzz")
#         else:
#             print(i)
# fizzbuzz()

# Maak een leeg woordenboek
telefoonboek = {}

while True:
    print("\n--- Telefoonboek ---")
    print("1. Voeg een contact toe")
    print("2. Bekijk contacten")
    print("3. Stop")
    keuze = input("Kies een optie (1-3): ")

    if keuze == "1":
        naam = input("Voer de naam in: ")
        nummer = input("Voer het telefoonnummer in: ")
        telefoonboek[naam] = nummer
        print(f"Contact {naam} toegevoegd.")
    elif keuze == "2":
        if telefoonboek:
            print("\nContacten:")
            for naam, nummer in telefoonboek.items():
                print(f"{naam}: {nummer}")
        else:
            print("Het telefoonboek is leeg.")
    elif keuze == "3":
        print("Programma gestopt.")
        break
    else:
        print("Ongeldige keuze, probeer opnieuw.")
