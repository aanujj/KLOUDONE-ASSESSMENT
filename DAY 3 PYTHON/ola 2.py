distance = int(input("input the distance in KM: "))         #asking how many miles have gone
time = int(input("input the time Hours: "))                          #asking how long it has taken
passengers = int(input("input the amount of passengers: "))    #asking how many passengers in the taxi

cost = distance * 20



if time > 5:
  cost= cost * 2



print (cost)