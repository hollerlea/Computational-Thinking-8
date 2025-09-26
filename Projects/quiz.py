genius = 0
dumb = 0
 

answer = input ("whats nine plus ten? A 19 B 21 ")
if answer == "A" or answer == "a":
    genius += 1
elif answer == "B" or answer == "b":
    dumb += 1
else:
    print (" Please pick A or B ")


answer = input ("would you rather play video games A or discover the laws of gravity B ")
if answer == "A" or answer == "a":
    dumb += 1
elif answer == "B" or answer == "b":
    genius += 1
else:
    dumb += 1


answer = input ("who was genghis kahn's best general? Sol Ganzorig A or Subutai B ")
if answer == "A"or answer == "a":
    dumb += 1
elif answer == "B" or answer == "b":
    genius += 1
else:
    dumb += 1



answer = input (" who was the 29th president? Warren G A or Herbert Hoover B ")
if answer == "A" or answer == "a":
    genius += 1
elif answer == "B" or answer == "b":
    dumb += 1
else:
    dumb += 1



answer = input ("how many presidents has there been? 48 A 47 B ")
if answer == "A"or answer == "a":
    dumb += 1
elif answer == "B" or answer == "b":
    genius += 1
else:
    dumb += 1
    



if genius > dumb:
    print ("you are a genius!")
elif dumb > genius:
    print ("you are dumb!")
if genius > dumb and 4:
    print ("you are the smartest! ")
elif dumb > genius and 4:
    ("you are really dumb!")