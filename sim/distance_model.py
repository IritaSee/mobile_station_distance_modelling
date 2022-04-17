# Initialise

n_station=3
stations = [[]]

# base stations, and another seperated by 200m
stations[0]=(100,71) 
print('Base stations coordiates: ')
print(stations[0])
for a in range(1,n_station-1):
    stations[a]=(stations[0][0]+200*a,stations[0][1])
    print(stations[a])

