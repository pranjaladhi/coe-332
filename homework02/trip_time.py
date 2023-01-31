#Pranjal Adhikari pa8729

import json
import math

with open ('random_sites.json', 'r') as s:
    sites_d = json.load(s)

print("\nROBOT SITE VISIT SUMMARY\n")


lat1 = 16.0
lon1 = 82.0
max_speed = 10
mars_radius = 3389.5

total_travel_time = 0

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:
    lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))
    return ( mars_radius * d_sigma )

for i in range (len(sites_d['sites'])): #stony-iron sample time
    lat2 = sites_d['sites'][i]['latitude']
    lon2 = sites_d['sites'][i]['longitude']
    
    time_to_site = calc_gcd(lat1, lon1, lat2, lon2) / max_speed
    total_travel_time += time_to_site

    print("Leg: ", i+1, ", time to travel = ", round(time_to_site, 2), " hr, ", end = " ")

    if sites_d['sites'][i]['meteorite composition'] == 'stony-iron':
        total_travel_time += 3
        print("time to sample = ", " 3 hr")

    elif sites_d['sites'][i]['meteorite composition'] == 'iron': #iron sample time
        total_travel_time += 2
        print("time to sample = ", " 2 hr")

    else: #stony sample time
        total_travel_time += 1
        print("time to sample = ", " 1 hr")

    lat1 = lat2
    lon1 = lon2

print("===============================================================")
print("Number of legs = ", len(sites_d['sites']), ", total time elapsed = ", round(total_travel_time, 2), " hr")