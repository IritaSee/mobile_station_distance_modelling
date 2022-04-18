import random
import math

def distance(veh,station):
    x1 = veh[0]
    y1 = veh[1]
    x2 = station[0]
    y2 = station[1] 
    result = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
    return result

# Initialise
n_station=int(input("Stations: "))
stations = [[]]

# base stations, and another seperated by 200m
stations[0]=(100,71)
#stations.append((stations[0][0]+200*1,stations[0][1]))
print('Base stations coordiates: ')
for a in range(1,n_station):
    stations.append((stations[0][0]+(200*a),stations[0][1]))

print(stations)

print()
# configure vehicles and motorway
n_vehicles = int(input("Vehicles: "))
n_rows = int(input("Motorway Lanes: "))
row_width = float(input("Per Lane Width: "))
vehicle_width = row_width/2
x_limit = int(input("X limit: "))

vehicles = []

print("vehicles coordinates:")
# generate random x and y value for vehicles
for a in range(n_vehicles):
    x = round(random.random()*x_limit)
    y = abs(round(random.random()*n_rows-1))
    y = (y*row_width)+vehicle_width
    vehicles.append((x,y))

print(vehicles)

print()
print("distances: ")
# count each vehicle distances to stations
for a in range(n_vehicles):
    print("For vehicle ",vehicles[a])
    for b in range(n_station):
        print("with station ",stations[b],": ",distance(vehicles[a],stations[b]))
    print()